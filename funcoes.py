#funções do jogo
import math
import random
import dados 

# Normalizando Base de Países - transforma banco de dados em dicionario cujas chave são paises
def normaliza(DADOS):
    saida = {}
    for continente in DADOS.keys():
        for pais in DADOS[continente]:
            
            conteudo = DADOS[continente][pais]
            
            saida[pais] = conteudo
            saida[pais]['continente'] = continente

    return saida



# Distância de Haversine - calcula distancia entre país selecinado e o sorteado 
def haversine(fi1, l1, fi2, l2):
    latitude1_rad = fi1*math.pi/180
    latitude2_rad = fi2*math.pi/180
    longitude1_rad = l1*math.pi/180
    longitude2_rad = l2*math.pi/180

    dif1 = (latitude2_rad-latitude1_rad)/2
    dif2 = (longitude2_rad-longitude1_rad)/2

    a = (math.sin(dif1))**2
    b = (math.sin(dif2))**2

    c = math.cos(latitude1_rad)*math.cos(latitude2_rad)
    angulo = math.sqrt(a+c*b)
    distancia = 2 * dados.EARTH_RADIUS * math.asin(angulo)
    
    return (f'{int(distancia):,}').replace(',','.')


# Sorteando Países - Escolhe país que deve ser adivinhado 
#dar .lower() no pais esolhido pelo jogador 
def sorteia_pais(dic):
    sorteio = random.choice(list(dic.keys()))
    return sorteio 



# Está na Lista? - verifica se o pais escolhido pelo user está no dicionario 
# tem que criar lista com os nomes dos paises
def esta_na_lista(pais, listas):
    pais=pais.lower()
    for lista in listas:
        if pais == lista:
            return True
    return False


# Adicionando em uma Lista Ordenada - retorna uma lista crescente com as distancias dos paises ja selecionados pelo jogador 
def adiciona_em_ordem(nome, distancia, lista):
    lista_1=[nome, distancia]
    lista_ordenada=[]
    contador=0
    if lista==[]:
        lista_ordenada.append(lista_1)
    else:
        for h in range(len(lista)):
            if nome==lista[h][0]:
                return lista
                break
    
        for i in range(len(lista)):
            if distancia<=lista[i][1]:
                lista_ordenada.append(lista_1)
                lista_ordenada.append([lista[i][0], lista[i][1]])
                contador=i
                break
    
            else:
                lista_ordenada.append([lista[i][0], lista[i][1]])
        if distancia>=lista[len(lista)-1][1]:
            lista_ordenada.append(lista_1)
        elif contador+1<len(lista):
            for k in range(contador+1,len(lista)):
                lista_ordenada.append([lista[k][0], lista[k][1]])
        
    
    return lista_ordenada



# Sorteia Letra com Restrições - sorteia uma letra da capital
#  Colocar letras ja sorteadas na lista de restrições
def sorteia_letra_capital(palavra, lista_restrita):

    especiais = ['.', ',', '-', ';', ' ', '@', '!', '$', '%', '*', '(', ')', '{', '}', '[', ']', ':']
    saida = ''
    palavra = palavra.lower()
    palavra_lista = []
    continua = False

    for letra in palavra:

        if letra not in especiais and letra not in lista_restrita and letra not in palavra_lista:
            palavra_lista.append(letra)
            continua = True

    while continua:
        saida = random.choice(palavra_lista)
        continua = False

    return saida

# Sorteia uma cor da bandeira
# Colocar tbm lista de restrição com as cores ja sorteadas
def cor_bandeira(bandeira, lista_restrita):

    cores_possiveis = []
    saida = ''

    for cor, quant in bandeira.items():
        if quant > 0:
            cores_possiveis.append(cor)

    saida = random.choice(cores_possiveis)
    
    if saida == 'outras' or saida in lista_restrita:
        while saida == 'outras'or saida in lista_restrita:
            saida = random.choice(cores_possiveis)

    return saida
# se ele ja sorteou todas as cores possiveis, retorna uma lista vazia



#inicializa os dados do pais sorteado
def cria_dicionario_pais_sorteado(pais,dicionario):
    dicionario_pais_sorteado = {}
    dicionario_pais_sorteado["nome"] = pais
    dicionario_pais_sorteado["latitude"] = dicionario[pais]['geo']['latitude']
    dicionario_pais_sorteado["longitude"] = dicionario[pais]['geo']['longitude']
    dicionario_pais_sorteado["area"] = dicionario[pais]['area']
    dicionario_pais_sorteado["populacao"] = dicionario[pais]['populacao']
    dicionario_pais_sorteado["capital"] = dicionario[pais]['capital']
    dicionario_pais_sorteado["bandeira"] = dicionario[pais]['bandeira']
    dicionario_pais_sorteado["continente"] = dicionario[pais]['continente']
    return dicionario_pais_sorteado


#debita tentativas
def debita_tentativa(total, debito, tentativas, entrada):
    if entrada not in tentativas.keys():
        if(total > debito):
            return total-debito
        return 0
    return total

def adiciona_tentativa(entrada,distancia_tentativa,distancias):
    distancias[entrada] = entrada + ' : ' + distancia_tentativa + ' km'
    return distancias

def atualiza_dicas_permitidas(dicas_permitidas,quantidade_tentativas):
    dicas_permitidas['1']=False
    dicas_permitidas['2']=False
    dicas_permitidas['3']=False
    dicas_permitidas['4']=False
    dicas_permitidas['5']=False
    if(quantidade_tentativas>4):
        dicas_permitidas['1']=True
    if(quantidade_tentativas>3):
        dicas_permitidas['2']=True
    if(quantidade_tentativas>6):
        dicas_permitidas['3']=True
    if(quantidade_tentativas>5):
        dicas_permitidas['4']=True
    if(quantidade_tentativas>7):
        dicas_permitidas['5']=True
    return dicas_permitidas

def dicionario_cores(cor):
    cores={}
    cores['preto']=30
    cores['vermelho']=31
    cores['verde']=32
    cores['amarelo']=33
    cores['azul']=34
    cores['magenta']=35
    cores['ciano']=36
    cores['cinza_claro']=37
    cores['branco']=97
    return cores[cor]

def dicionario_cores_fundo(cor_fundo):
    cores_fundo={}
    cores_fundo['preto']=40
    cores_fundo['vermelho']=41
    cores_fundo['verde']=42
    cores_fundo['amarelo']=43
    cores_fundo['azul']=44
    cores_fundo['magenta']=45
    cores_fundo['ciano']=46
    cores_fundo['cinza_claro']=47
    cores_fundo['branco']=107
    return cores_fundo[cor_fundo]
