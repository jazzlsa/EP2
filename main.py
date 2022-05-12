from asyncio.windows_events import NULL
from dis import dis
from dados import DADOS
import funcoes
import display

continuar ='s' #inicia continuar
dicas_compradas = [] #inicia dicas compradas
lista_paises = []
ganhou = False #inicia ganhou
desistiu = False #inicia desistiu
pais_sorteado = NULL #inicia o pais sorteado
dados_normalizados = funcoes.normaliza(DADOS) # Dicionario com os países (como chave) e seus respectivos dados
distancias = [] #inicializando as distancias das tentativas

# Colocando os países na lista
for pais in dados_normalizados.keys():
  lista_paises.append(pais)

while continuar == 's': # laço para garantir que ele continue jogando até dizer que não
  #inicia quantidade de tentativas
  quantidade_tentativas = 20
  #define qual o país para se ganhar
  pais_sorteado = funcoes.cria_dicionario_pais_sorteado(funcoes.sorteia_pais(dados_normalizados),dados_normalizados)
  #mostra as boas vindas do jogo
  display.display_boas_vindas()
  #mostra o menu
  display.display_menu()

  #continua não tiver desistido ou ganhado ou tiver tentativas
  while quantidade_tentativas != 0 or ganhou == False or desistiu == False:
    #pega o que ele for digitar
    entrada = input('Qual é o país sorteado? ')
    #dar .lower() no pais esolhido pelo jogador 
    
    #pula linha
    print()

    if funcoes.esta_na_lista(entrada, dados_normalizados)==True and (entrada != pais_sorteado['nome']):
      #queima uma tentativa
      quantidade_tentativas=funcoes.debita_tentativa(quantidade_tentativas,1)
      #verifica a distância do país informado com o país sorteado
      distancia_tentativa = funcoes.haversine(pais_sorteado['latitude'], pais_sorteado['longitude'], dados_normalizados[entrada]['geo']['latitude'], dados_normalizados[entrada]['geo']['longitude'])
      #adiciona a distância do país informado a lista de tentativas
      distancias.append(entrada+': '+distancia_tentativa+'km')
      #mostra todas as distancias
      display.display_distancias(distancias)
      #mostra o restante das tentativas
      display.display_tentativas_restantes(quantidade_tentativas)
    else:
      if(entrada=='menu'):
        display.display_menu()
      if(entrada=='dica'):
        display.display_mercado_dicas()
      if(entrada=='desisto'):
        display.display_confirma_desisto()
        entrada = input()
        while(entrada!='s' and entrada!='n'):
          display.display_confirma_desisto()
        if(entrada=='s'):
          display.display_sim_desisto()
          desistiu=True
        if(entrada=='n'):
          display.display_nao_desisto()
      if(entrada=='inventario'):
        print('Não sei o que é isso')
      if(entrada not in ['menu','dica','desisto']):
        print('Eita! O valor digitado não é um país. Lembre-se de não digitar acentos e letras maiúsculas')

# 
# 
# 
#    tentativa-=1
#        latitude_entrada =
#        longitude_entrada =brasi
#			  distancia = funcoes.haversine()  #verifica se o que foi digitado é um pais, se for diminui a tentativa e atualiza distancia

#			display_adiciona em ordem(pais, distancia) #mostra as distancias das tentativas
			
#      else
#        ganhou = true #seta que ganhou
#      elif esta_na_lista(entrada, lista)==False:
#        display_pais_desconhecido			
#      if(entrada = dica) #verifica se ele quer comprar dicas
#        while entrada not in dicas ou entrada != cancelar:
#          display_menu_dicas(dicas_compradas) #mostra as opções do mercado de dicas que ainda não foram compradas
#          entrada = input() #pega o que ele for digitar
#          dicas_compradas = dicas(entrada, quantidade_tentativas, dicas_compradas) #diminui a quantidade de tentativas e atualiza as dicas compradas
#          display_dicas_compradas(dicas_compradas) #mostra todas as dicas compradas


#  print('Perdeu! O país era {}')
#  continuar=input('Jogar Novamente?s/n ')
#  while continuar!='s' and continuar!='n':
#    continuar=input('Ops! Não entendi. Digite s/n: ')