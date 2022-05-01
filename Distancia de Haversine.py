import math
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

import random
def sorteia_pais(dic):
    sorteio=random.choice(list(dic.keys()))
    return sorteio 