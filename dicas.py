'''
Mercado de Dicas
----------------------------------------
1. Cor da bandeira  - custa 4 tentativas
2. Letra da capital - custa 3 tentativas
3. Área             - custa 6 tentativas
4. População        - custa 5 tentativas
5. Continente       - custa 7 tentativas
0. Sem dica
----------------------------------------
Escolha sua opção [0|1|2|3|4|5]: 

'''
entrada = {
  "afeganistao": {
    "area": 652230,
    "populacao": 31390200,
    "capital": "Cabul",
    "geo": {
      "latitude": 33.93911,
      "longitude": 67.709953
    },
    "bandeira": {
      "vermelha": 28,
      "laranja": 1,
      "amarela": 0,
      "verde": 33,
      "azul": 0,
      "azul claro": 0,
      "preta": 33,
      "branca": 3,
      "outras": 5
    },
    "continente": "asia"}}

cor_bandeira = entrada["afeganistao"]["bandeira"]
letra_capital = entrada["afeganistao"]["Cabul"]
area = entrada["afeganistao"]["area"]
pop = entrada["afeganistao"]["populacao"]
continente = entrada["afeganistao"]["continente"]
na = ''


from os import popen


def dicas(num):

    dicas = {
        '1' : cor_bandeira,
        '2' : letra_capital,
        '3' : area,
        '4' : pop,
        '5' : continente,
        '0' : na,
    }
