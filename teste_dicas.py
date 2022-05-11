import funcoes

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

pais_sorteado = 'afeganistão'
lista_restrita_capital = []
capital = entrada["afeganistao"]['capital']

def dicas(num_escolhido):

    print(lista_restrita_capital)

    dicas_dic = {
        '1' : ['', '4'],
        '2' : [funcoes.sorteia_letra_capital(capital, lista_restrita_capital), '3'],
        '3' : ['', '6'],
        '4' : ['', '5'],
        '5' : ['', '7']
    }

    dados = dicas_dic[num_escolhido]

    dica = dados[0]
    tentativas_gastas = dados[1]

    #if num_escolhido == '2':
    #    lista_restrita_capital.append(dica)   ----> vai ter que adicionar isso fora da função (o mesmo para a bandeira)

    return dica, tentativas_gastas 

print(dicas('2'))

# o que vai pro main




'''
    1. Cor da bandeira  - custa 4 tentativas
2. Letra da capital - custa 3 tentativas
3. Área             - custa 6 tentativas
4. População        - custa 5 tentativas
5. Continente       - custa 7 tentativas
0. Sem dica
'''