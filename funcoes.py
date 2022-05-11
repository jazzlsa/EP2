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

    return distancia 


# Sorteando Países - Escolhe país que deve ser adivinhado 
#dar .lower() no pais esolhido pelo jogador 
def sorteia_pais(dic):
    sorteio = random.choice(list(dic.keys()))
    return sorteio 



# Está na Lista? - verifica se o pais escolhido pelo user está no dicionario 
# tem que criar lista com os nomes dos paises
def esta_na_lista(pais, listas):
    for lista in listas:
        if pais in lista:
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

dados_normalizados = normaliza(dados.DADOS)
pais = sorteia_pais(dados_normalizados)
bandeira = dados_normalizados[pais]['bandeira']

lista_restrita = ['azul claro', 'verde', 'amarela', 'vermelha']

print(cor_bandeira(bandeira, lista_restrita))

