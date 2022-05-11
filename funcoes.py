import math
import random
import dados 



def haversine(raio, fi1, l1, fi2, l2):
    latitude1_rad=fi1*math.pi/180
    latitude2_rad=fi2*math.pi/180
    longitude1_rad=l1*math.pi/180
    longitude2_rad=l2*math.pi/180
    dif1=(latitude2_rad-latitude1_rad)/2
    dif2=(longitude2_rad-longitude1_rad)/2
    a= (math.sin(dif1))**2
    b= (math.sin(dif2))**2
    c=math.cos(latitude1_rad)*math.cos(latitude2_rad)
    angulo=math.sqrt(a+c*b)
    distancia=2*raio*math.asin(angulo)
    return distancia 

def sorteia_pais(dic):
    sorteio=random.choice(list(dic.keys()))
    return sorteio 

def esta_na_lista(pais, listas):

    for lista in listas:
        if pais in lista:
            return True

    return False
 
def adiciona_em_ordem(nome, distancia, lista):
    lista_1=[nome, distancia]
    lista_ordenada=[]
    contador=0
    if lista==[]:
        lista_ordenada.append(lista_1)
    else:
        
        for i in range(len(lista)):
            if distancia<=lista[i][1]:
                lista_ordenada.append(lista_1)
                lista_ordenada.append([lista[i][0], lista[i][1]])
                contador=i
                break
    
            else:
                lista_ordenada.append([lista[i][0], lista[i][1]])
        if contador+1<=len(lista):
            for k in range(contador+1,len(lista)):
                lista_ordenada.append([lista[k][0], lista[k][1]])
        if distancia>=lista[len(lista)-1][1]:
            lista_ordenada.append(lista_1)
    
    return lista_ordenada

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
    
def cor_bandeira(bandeira):

    cores_possiveis = []
    saida = ''

    for cor, quant in bandeira.items():
        if quant > 0:
            cores_possiveis.append(cor)

    saida = random.choice(cores_possiveis)
    
    if saida == 'outras':
        saida = random.choice(cores_possiveis)

    return saida

def normaliza(dic):

    saida = {}

    for continente in dic.keys():
        for pais in dic[continente]:
            
            conteudo = dic[continente][pais]
            
            saida[pais] = conteudo

            saida[pais]['continente'] = continente
            
    return saida
