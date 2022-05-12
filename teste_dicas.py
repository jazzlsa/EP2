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

pais_sorteado = 'afeganistao'
area_pais_sorteado = entrada[pais_sorteado]['area']
populacao_pais_sorteado = entrada[pais_sorteado]['populacao']
capital_pais_sorteado = entrada[pais_sorteado]['capital']
bandeira_pais_sorteado = entrada[pais_sorteado]['bandeira']
continente_pais_sorteado = entrada[pais_sorteado]['continente']

lista_restrita_capital = []
lista_restrita_bandeira = []


def dicas(num_escolhido):
    dicas_dic = {
        '1' : [funcoes.cor_bandeira(bandeira_pais_sorteado, lista_restrita_bandeira), '4', 'Cor da Bandeira: '],
        '2' : [funcoes.sorteia_letra_capital(capital_pais_sorteado, lista_restrita_capital), '3', 'Letra da capital: '],
        '3' : ['area_pais_sorteado', '6', 'Área: '],
        '4' : ['populacao_pais_sorteado', '5', 'População: '],
        '5' : ['continente_pais_sorteado', '7', 'Continente: ']
    }

    dados = dicas_dic[num_escolhido]

    dica = dados[0]
    tentativas_gastas = dados[1]
    identificador = dados[2]

    #if num_escolhido == '2':
    #    lista_restrita_capital.append(dica)   ----> vai ter que adicionar isso fora da função (o mesmo para a bandeira)

    return dica, tentativas_gastas, identificador


# o que vai pro main
# colocar restrição para caso a bandeira e a letra da capital não tenham mais opções
# Fazer dicionario adicionaçl para os prints - dai da pra remover 
lista_restrita_capital = []
lista_restrita_bandeira = []

num = input('Escolha sua opção [0|1|2|3|4|5]: ')

retorno_funcao = dicas(num)

dica = retorno_funcao[0]
custo_tentativa = retorno_funcao[1]
identificador = retorno_funcao[2]

print(dica,
custo_tentativa,
identificador)

