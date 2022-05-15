import funcoes
import display

pais_sorteado = {
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

def dicas(entrada_dicas, pais_sorteado, lista_restrita_bandeira, lista_restrita_capital):
    pais = 'afeganistao'

    area_pais_sorteado = pais_sorteado[pais]['area']
    populacao_pais_sorteado = pais_sorteado[pais]['populacao']
    capital_pais_sorteado = pais_sorteado[pais]['capital']
    bandeira_pais_sorteado = pais_sorteado[pais]['bandeira']
    continente_pais_sorteado = pais_sorteado[pais]['continente']

    dicas_dic = {
        '1' : [funcoes.cor_bandeira(bandeira_pais_sorteado, lista_restrita_bandeira), '4', 'Cor da Bandeira: '],
        '2' : [funcoes.sorteia_letra_capital(capital_pais_sorteado, lista_restrita_capital), '3', 'Letra da capital: '],
        '3' : [area_pais_sorteado, '6', 'Área: '],
        '4' : [populacao_pais_sorteado, '5', 'População: '],
        '5' : [continente_pais_sorteado, '7', 'Continente: '],
    }

    dados = dicas_dic[entrada_dicas]
    dica = dados[0]
    tentativas_gastas = dados[1]
    identificador = dados[2]

    return dica, tentativas_gastas, identificador


# o que vai pro main
# colocar restrição para caso a bandeira e a letra da capital não tenham mais opções
# Fazer dicionario adicionaçl para os prints - dai da pra remover 
continuar = True
lista_restrita_capital = []
lista_restrita_bandeira = []
dicas_ja_foram = {}
dic_dicas = {}
nova_dica = ''
quantidade_tentativas = 10

while continuar:

  simulacao = True

  while simulacao:
    nova_dica = ''

    print('Mercado de Dicas')
    print('✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ')
    print('1. Cor da bandeira  - custa 4 tentativas')
    print('2. Letra da capital - custa 3 tentativas')
    print('3. Área             - custa 6 tentativas')
    print('4. População        - custa 5 tentativas')
    print('5. Continente       - custa 7 tentativas')
    print('0. Sem dica')
    print('✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ')
    entrada_dicas = input('Escolha sua opção [0|1|2|3|4|5]: ')

    retorno_funcao = dicas(entrada_dicas, pais_sorteado, lista_restrita_bandeira, lista_restrita_capital)

    dica = retorno_funcao[0]
    custo_tentativa = int(retorno_funcao[1])
    identificador = retorno_funcao[2]

    print(custo_tentativa)

    nova_dica = '- {}{}'.format(identificador, dica)

    if entrada_dicas == '1':
      lista_restrita_bandeira.append(dica)
    if entrada_dicas == '2':
      lista_restrita_capital.append(dica)

'''
    def adiciona_dicas_usadas(nova_dica, dicas_ja_foram, entrada_dicas, dica):

      if entrada_dicas not in dicas_ja_foram.keys():
        dicas_ja_foram[entrada_dicas] = nova_dica

      elif entrada_dicas == '1':
        dicas_ja_foram[entrada_dicas] += ', {}'.format(dica)
      elif entrada_dicas == '2':
        dicas_ja_foram[entrada_dicas] += ', {}'.format(dica)

      return dicas_ja_foram

    dic_dicas = adiciona_dicas_usadas(nova_dica, dicas_ja_foram, entrada_dicas, dica)

    def display_dicas_ja_foram(dic_dicas):
      for ea in dic_dicas.values():
        print(ea)

    eae = display_dicas_ja_foram(dic_dicas)

    simulacao = False

    respost = input('quer continuar? ')
    if respost == 'n':
      continuar = False
'''