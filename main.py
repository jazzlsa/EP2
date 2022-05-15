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
  # dicionário de dicas
  dic_dicas = {}
  # Inicializa as dicas que já foram compradas
  dicas_ja_foram = {} 
  # Inicializa lista que impede letras de se repetirem ao pedir a dica '2'
  lista_restrita_capital = []
  # Inicializa lista que impede as cores de se repetirem ao pedir a dica '1'
  lista_restrita_bandeira = []
  #inicia dicas compradas
  dicas_compradas = []
  #inicializando as distancias das tentativas
  distancias = {}
  #inicia ganhou
  ganhou = False
  #inicia desistiu
  desistiu = False
  #inicia quantidade de tentativas
  quantidade_tentativas = 20
  #inicia dicas permitidas
  dicas_permitidas = {'0':True,'1':True,'2':True,'3':True,'4':True,'5':True}
  dicas_permitidas = funcoes.atualiza_dicas_permitidas(dicas_permitidas,quantidade_tentativas,'')
  #define qual o país para se ganhar
  pais_sorteado = funcoes.cria_dicionario_pais_sorteado(funcoes.sorteia_pais(dados_normalizados),dados_normalizados)
  pais_sorteado['bandeira'] = funcoes.normaliza_cores_bandeira(pais_sorteado['bandeira'])
  #mostra as boas vindas do jogo
  display.display_boas_vindas()
  #mostra o menu
  display.display_menu()
  display.display_tentativas_restantes(quantidade_tentativas)
  print()

  #continua não tiver desistido ou ganhado ou tiver tentativas
  while quantidade_tentativas != 0 and ganhou == False and desistiu == False:
    #pega o que ele for digitar
    entrada = input('\033[1;35mQual é o país sorteado?\033[m ')
    entrada = entrada.lower()
    #pula linha
    print()

    if funcoes.esta_na_lista(entrada, dados_normalizados)==True and (entrada != pais_sorteado['nome']):
      #queima uma tentativa
      quantidade_tentativas=funcoes.debita_tentativa(quantidade_tentativas,1,distancias,entrada)
      #atualiza as dicas permitidas
      dicas_permitidas = funcoes.atualiza_dicas_permitidas(dicas_permitidas,quantidade_tentativas,'')
      #verifica a distância do país informado com o país sorteado
      distancia_tentativa = funcoes.haversine(pais_sorteado['latitude'], pais_sorteado['longitude'], dados_normalizados[entrada]['geo']['latitude'], dados_normalizados[entrada]['geo']['longitude'])
      #Adiciona distâncias na lista de tentativas
      distancias = funcoes.adiciona_tentativa(entrada,distancia_tentativa,distancias)
      
      #mostra todas as distancias
      display.display_distancias(distancias)
      #mostra o restante das tentativas
      display.display_tentativas_restantes(quantidade_tentativas)
    else:
      #mostra menu
      if(entrada=='menu'):
        display.display_menu()
        
      #mostra confirmação de desistência
      if(entrada=='desisto'):
        display.display_confirma_desisto()
        entrada = input()
        #laço para o usuário digitar apenas S ou N
        while(entrada!='s' and entrada!='n'):
          display.display_confirma_desisto()
          entrada = input()
        #confirmação de desistencia
        if(entrada=='s'):
          #mostra mensagem de desistencia
          display.display_sim_desisto()
          desistiu=True
          entrada='desisto'
        #negação de desistencia
        if(entrada=='n'):
          #mostra mensagem de negação de desistencia
          display.display_nao_desisto()
          entrada='desisto'

      # mostra inventário
      if(entrada=='inventario'):
      
        print('\033[;1m✿ ❀ PAISES JÁ TESTADOS ✿ ❀ ✿\033[m')
        if(len(distancias)==0):
          print('\033[1;35mNenhum país testado\033[m')
        else:
          display.display_distancias(distancias)
        print()

        print('\033[;1m✿ ❀ DICAS JÁ COMPRADAS ✿ ❀ ✿\033[m')
        if(len(dic_dicas)==0):
          print('\033[1;35mNenhuma dica comprada\033[m')
        else:
          dica = display.display_dicas_ja_foram(dic_dicas)
        print()

      # mostra e avalia as dicas existentes -  caso o jogador escolha "dica"
      if(entrada=='dica'):
        entrada_dicas = NULL
        entrada_dicas = display.display_mercado_dicas(dicas_permitidas)
        digito_correto = False

        while(entrada_dicas not in dicas_permitidas or dicas_permitidas[entrada_dicas]==False):
          display.erro_digito_opcao_dicas()
          entrada_dicas = input('\033[1;35mTenta de novo, qual é a opção que você deseja?\033[m ')
        
        if(entrada_dicas!='0'):
          nova_dica = ''

          retorno_funcao = funcoes.dicas(entrada_dicas, pais_sorteado, lista_restrita_bandeira, lista_restrita_capital,dicas_permitidas,quantidade_tentativas)

          dica = retorno_funcao[0]
          custo_tentativa = int(retorno_funcao[1])
          identificador = retorno_funcao[2]

          nova_dica = '- {}{}'.format(identificador, dica)

          if entrada_dicas == '1':
            lista_restrita_bandeira.append(dica)
            if(len(lista_restrita_bandeira)==len(pais_sorteado['bandeira'])):
              dicas_permitidas = funcoes.atualiza_dicas_permitidas(dicas_permitidas,quantidade_tentativas,'1')
          if entrada_dicas == '2':
            lista_restrita_capital.append(dica)
          if(entrada_dicas == '3'):
            dicas_permitidas = funcoes.atualiza_dicas_permitidas(dicas_permitidas,quantidade_tentativas,'3')
          if(entrada_dicas == '4'):
            dicas_permitidas = funcoes.atualiza_dicas_permitidas(dicas_permitidas,quantidade_tentativas,'4')
          if(entrada_dicas == '5'):
            dicas_permitidas = funcoes.atualiza_dicas_permitidas(dicas_permitidas,quantidade_tentativas,'5')

          dic_dicas = funcoes.adiciona_dicas_usadas(nova_dica, dicas_ja_foram, entrada_dicas, dica)
          tela = display.display_dicas_ja_foram(dic_dicas)

          if dica != '': # Condição que impede de descontar as tentativas caso ja tenha conseguido todas as letras da capital ou todas as cores da bandeira
            quantidade_tentativas=funcoes.debita_tentativa(quantidade_tentativas,custo_tentativa,distancias,entrada)
            dicas_permitidas = funcoes.atualiza_dicas_permitidas(dicas_permitidas,quantidade_tentativas,'')
          
          display.display_tentativas_restantes(quantidade_tentativas)
        
      #verifica se não é uma das opções. Se não for mostra msg de informação errada
      if entrada not in ['menu','dica','desisto','inventario'] and entrada != pais_sorteado['nome']:
        print('\033[1;35mEita! O valor digitado não é um país. Lembre-se de não digitar acentos.\033[m')
      #verifica se o pais digitado é o correto
      if(entrada==pais_sorteado['nome']):
        ganhou = True
  #mostra mensagem caso tenha perdido
  if(ganhou == False):
    print('\033[1;35mIhhh! Não foi dessa vez, meu chapa! O país era '+pais_sorteado['nome']+', fechou?\033[m')
    print()
  #mostra mensagem caso tenha ganhado
  if(ganhou == True):
    display.ganhou1()
    print()
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
  entrada='desisto'
#mostra mensagem final
display.produtivo()