from dados import DADOS
import funcoes

continuar ='s' #inicia continuar

dicas_compradas = [] #inicia dicas compradas

lista_paises = []

ganhou = False #inicia ganhou

desistiu = False #inicia desistiu

dados_normalizados = funcoes.normaliza(DADOS) # Dicionario com os países (como chave) e seus respectivos dados

for pais in dados_normalizados.keys(): # Colocando os países na lista
  lista_paises.append(pais)


#while continuar == 's': # laço para garantir que ele continue jogando até dizer que não

  quantidade_tentativas = 20 #inicia quantidade de tentativas

  pais_sorteado = funcoes.sorteia_pais(dados_normalizados) #define qual o país para se ganhar
  print(pais_sorteado)
  
  latitude_pais_sorteado = dados_normalizados[pais_sorteado]['geo']['latitude']
  longitude_pais_sorteado = dados_normalizados[pais_sorteado]['geo']['longitude']
  area_pais_sorteado = dados_normalizados[pais_sorteado]['area']
  populacao_pais_sorteado = dados_normalizados[pais_sorteado]['populacao']
  capital_pais_sorteado = dados_normalizados[pais_sorteado]['capital']
  bandeira_pais_sorteado = dados_normalizados[pais_sorteado]['bandeira']
  continente_pais_sorteado = dados_normalizados[pais_sorteado]['continente']

<<<<<<< HEAD
  sorteia_pais(dados_normalizados) #define qual o país para se ganhar

  latitude_pais_sorteado =
  longitude_pais_sorteado =
=======
>>>>>>> 469ea1fe715b67cff314f0f83aeb75d6dad463e8

  display_boas_vindas() #mostra as boas vindas do jogo

  while tentativas!=0:

	  display_menu() #mostra o menu de como continuar jogando, desistir ou dicas

	  while quantidade_tentativas > 0 or ganhou = False or desistiu = False #continua o jogo enquanto não tiver desistido, não tiver ganhado ou ainda tiver tentativas

		entrada = input('Qual país? ') #pega o que ele for digitar

      if esta_na_lista(entrada, lista_paises)==True and (entrada != pais):
        tentativa-=1
        latitude_entrada =
        longitude_entrada =
			  distancia = funcoes.haversine()  #verifica se o que foi digitado é um pais, se for diminui a tentativa e atualiza distancia

			display_adiciona em ordem(pais, distancia) #mostra as distancias das tentativas
			
      else
        ganhou = true #seta que ganhou
      elif esta_na_lista(entrada, lista)==False:
        display_pais_desconhecido			
      if(entrada = dica) #verifica se ele quer comprar dicas
        while entrada not in dicas ou entrada != cancelar:
          display_menu_dicas(dicas_compradas) #mostra as opções do mercado de dicas que ainda não foram compradas
          entrada = input() #pega o que ele for digitar
          dicas_compradas = dicas(entrada, quantidade_tentativas, dicas_compradas) #diminui a quantidade de tentativas e atualiza as dicas compradas
          display_dicas_compradas(dicas_compradas) #mostra todas as dicas compradas


  print('Perdeu! O país era {}')
  continuar=input('Jogar Novamente?s/n ')
  while continuar!='s' and continuar!='n':
    continuar=input('Ops! Não entendi. Digite s/n: ')
'''