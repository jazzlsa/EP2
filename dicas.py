from funcoes_para_dicas import *

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
lista_restrita = []

cor = cor_bandeira(entrada["afeganistao"]["bandeira"])
letra_capital = sorteia_letra_capital(entrada["afeganistao"]["capital"], lista_restrita)
area = entrada["afeganistao"]["area"]
pop = entrada["afeganistao"]["populacao"]
continente = entrada["afeganistao"]["continente"]
na = ''

cores_sorteadas = []

def dicas(num):

  # Pegando cor da bandeira 
  cor = cor_bandeira(entrada["afeganistao"]["bandeira"])

  if cor in cores_sorteadas:
    cor = cor_bandeira(entrada["afeganistao"]["bandeira"])

  return cor
