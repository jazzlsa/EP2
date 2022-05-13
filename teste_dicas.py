import funcoes

dicionario_pais_sorteado = {
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

def dicas(num_escolhido):
  
    area_pais_sorteado = dicionario_pais_sorteado[pais_sorteado]['area']
    populacao_pais_sorteado = dicionario_pais_sorteado[pais_sorteado]['populacao']
    capital_pais_sorteado = dicionario_pais_sorteado[pais_sorteado]['capital']
    bandeira_pais_sorteado = dicionario_pais_sorteado[pais_sorteado]['bandeira']
    continente_pais_sorteado = dicionario_pais_sorteado[pais_sorteado]['continente']

    dicas_dic = {
        '1' : [funcoes.cor_bandeira(bandeira_pais_sorteado, lista_restrita_bandeira), '4', 'Cor da Bandeira: '],
        '2' : [funcoes.sorteia_letra_capital(capital_pais_sorteado, lista_restrita_capital), '3', 'Letra da capital: '],
        '3' : [area_pais_sorteado, '6', 'Área: '],
        '4' : [populacao_pais_sorteado, '5', 'População: '],
        '5' : [continente_pais_sorteado, '7', 'Continente: ']
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
continuar = True
lista_restrita_capital = []
lista_restrita_bandeira = []
dicas_ja_foram = []

while continuar:

  simulacao = True

  while simulacao:
    print('Mercado de Dicas')
    print('✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ')
    print('1. Cor da bandeira  - custa 4 tentativas')
    print('2. Letra da capital - custa 3 tentativas')
    print('3. Área             - custa 6 tentativas')
    print('4. População        - custa 5 tentativas')
    print('5. Continente       - custa 7 tentativas')
    print('0. Sem dica')
    print('✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ')
    num = input('Escolha sua opção [0|1|2|3|4|5]: ')
    dicas_ja_foram.append(num)

    retorno_funcao = dicas(num)

    dica = retorno_funcao[0]
    custo_tentativa = retorno_funcao[1]
    identificador = retorno_funcao[2]

    print(dica, custo_tentativa, identificador, dicas_ja_foram)

    simulacao = False

    respost = input('quer continuar? ')
    if respost == 'n':
      continuar = False
