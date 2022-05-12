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
  dicionario_pais_sorteado = funcoes.cria_dicionario_pais_sorteado(funcoes.sorteia_pais(dados_normalizados),dados_normalizados)
  pais_sorteado = dicionario_pais_sorteado["nome"]
  #mostra as boas vindas do jogo
  display.display_boas_vindas()
  #mostra o menu
  display.display_menu()

  #continua não tiver desistido ou ganhado ou tiver tentativas
  while quantidade_tentativas != 0 or ganhou == False or desistiu == False:
    #pega o que ele for digitar
    entrada = input('Qual é o país sorteado? ')
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
      #mostra menu
      if(entrada=='menu'):
        display.display_menu()
      #mostra dica e avalia as dicas existentes
      if(entrada=='dica'):
        display.display_mercado_dicas()
      #mostra confirmação de desistência
      if(entrada=='desisto'):
        display.display_confirma_desisto()
        entrada = input()
        #laço para o usuário digitar apenas S ou N
        while(entrada!='s' and entrada!='n'):
          display.display_confirma_desisto()
        #confirmação de desistencia
        if(entrada=='s'):
          #mostra mensagem de desistencia
          display.display_sim_desisto()
          desistiu=True
        #negação de desistencia
        if(entrada=='n'):
          #mostra mensagem de negação de desistencia
          display.display_nao_desisto()
      #mostra inventário
      if(entrada=='inventario'):
        print('Não sei o que é isso')
      #verifica se não é uma das opções. Se não for mostra msg de informação errada
      if(entrada not in ['menu','dica','desisto']):
        print('Eita! O valor digitado não é um país. Lembre-se de não digitar acentos.')

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