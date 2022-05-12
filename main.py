from asyncio.windows_events import NULL
from dis import dis
from dados import DADOS
import funcoes
import display

continuar ='s' #inicia continuar
lista_paises = []
pais_sorteado = NULL #inicia o pais sorteado
dados_normalizados = funcoes.normaliza(DADOS) # Dicionario com os países (como chave) e seus respectivos dados

# Colocando os países na lista
for pais in dados_normalizados.keys():
  lista_paises.append(pais)

#laço para garantir que ele continue jogando até dizer que não
while continuar == 's': 
  #inicia dicas compradas
  dicas_compradas = []
  #inicializando as distancias das tentativas
  distancias = {}
  #inicia ganhou
  ganhou = False
  #inicia desistiu
  desistiu = False
  #inicia quantidade de tentativas
  quantidade_tentativas = 3
  #define qual o país para se ganhar
  pais_sorteado = funcoes.cria_dicionario_pais_sorteado(funcoes.sorteia_pais(dados_normalizados),dados_normalizados)
  #mostra as boas vindas do jogo
  display.display_boas_vindas()
  #mostra o menu
  display.display_menu()

  #continua não tiver desistido ou ganhado ou tiver tentativas
  while quantidade_tentativas != 0 and ganhou == False and desistiu == False:
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
      #distancias.append(entrada+': '+distancia_tentativa+'km')

      funcoes.adiciona_tentativa(entrada,distancia_tentativa,distancias)
      
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
      if(entrada not in ['menu','dica','desisto','s','n']):
        print('Eita! O valor digitado não é um país. Lembre-se de não digitar acentos.')
      #verifica se o pais digitado é o correto
      if(entrada==pais_sorteado['nome']):
        ganhou = True
  #mostra mensagem caso tenha perdido
  if(ganhou==False):
    print('Ihhh! Não foi dessa vez, meu chapa! O país era '+pais_sorteado['nome']+', fechou?')
  #mostra mensagem caso tenha ganhado
  if(ganhou==True):
    display.ganhou1()
  #mostra mensagem se quer mais uma rodada
  display.jogar_novamente()
  entrada=''
  #laço para aceitar apenas s ou n
  while(entrada!='s' and entrada!='n'):
    entrada=input()
    #mostra mensagem dizendo que é apenas s ou n
    if(entrada!='s' and entrada!='n'):
      display.digite_s_ou_n()
  continuar=entrada
#mostra mensagem final
display.produtivo()