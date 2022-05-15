#funções de tela
import funcoes
from zmq import NULL


def display_boas_vindas():
    print('')
    with open('rapozinha.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        arquivo.close()

    raposinha = []
    for linha in linhas:
        raposinha.append(linha)
    for li in raposinha:
        print('\033[1;35m'+str(li)+'\033[m', end='')
    print('')

def display_menu():
    print('')
    print('\033[1;35mComandos:                                     \033[m')
    print('')
    print('\033[1;35mdica       - Entra no mercado de dicas\033[m')
    print('\033[1;35mdesisto    - Desiste da rodada        \033[m')
    print('\033[1;35minventario - Exibe sua posição        \033[m')
    print('\033[1;35mmenu       - Exibe este menu                             \033[m')
    print('')
    
def display_mercado_dicas(dicas_permitidas):
    string_opcoes=''
    tem_dicas = False
    for indice in dicas_permitidas.keys():
        if(dicas_permitidas[indice]==True and indice!='0'):
            tem_dicas=True
            break
    if(tem_dicas==False):
        print('\033[1;35mParceiro, infelizmente você não tem tentativas para comprar dicas, fechou?\033[m')
        print()
        return '0'
    
    print('')
    print('\033[1;95m✿ ❀ ✿ ❀ ✿  Mercado de Dicas ❀ ✿ ❀ ✿ ❀ ✿ ❀\033[m')
    print('')
    if(dicas_permitidas['1']):
        print('\033[1;95m1. Cor da bandeira  - custa 4 tentativas\033[m')
        string_opcoes=string_opcoes+'|1'
    if(dicas_permitidas['2']):
        print('\033[1;95m2. Letra da capital - custa 3 tentativas\033[m')
        string_opcoes=string_opcoes+'|2'
    if(dicas_permitidas['3']):
        print('\033[1;95m3. Área             - custa 6 tentativas\033[m')
        string_opcoes=string_opcoes+'|3'
    if(dicas_permitidas['4']):
        print('\033[1;95m4. População        - custa 5 tentativas\033[m')
        string_opcoes=string_opcoes+'|4'
    if(dicas_permitidas['5']):
        print('\033[1;95m5. Continente       - custa 7 tentativas\033[m')
        string_opcoes=string_opcoes+'|5'
    print('\033[1;95m0. Voltar                                     \033[m')
    print('')
    print('\033[1;95m✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿\033[m')
    print()
    entrada_dicas = input('\033[1;35mEscolha sua opção [0'+string_opcoes+']: \033[m')
    print()
    return entrada_dicas

def display_tentativas_restantes(tentativas):
    print('')
    if tentativas > 15:
        print('Você possui \033[1;35m'+str(tentativas)+'\033[m tentativas restantes')
    
    elif tentativas <= 15 and tentativas > 10:
        print('Você possui \033[1;33m'+str(tentativas)+'\033[m tentativas restantes')
    elif tentativas <= 10 and tentativas > 5:
        print('Você possui \033[1;32m'+str(tentativas)+'\033[m tentativas restantes')
    elif tentativas <= 10 and tentativas <= 5:
        print('Você possui \033[1;31m'+str(tentativas)+'\033[m tentativas restantes')
    print('')

def display_confirma_desisto():
    print('')
    print('\033[1;35mNão acredito que você seja um arregão. Quer mesmo desistir?\033[m')
    print('\033[1;35m[s/n]\033[m')

def display_nao_desisto():
    print('')
    print('\033[1;35mSabia que você não era um arregão!\033[m')
    print('')

def display_sim_desisto():
    print('')
    print('\033[1;35mSabia que você era um arregão!\033[m')
    print('')

def display_distancias(array_distancias):
    string = ''
    for distancias in array_distancias:
        string = distancias+' : '+(f'{int(array_distancias[distancias]):,}').replace(',','.')+' km'
        
        if array_distancias[distancias] > 10000:
            print('\033[1;31m'+string+'\033[m')
        elif array_distancias[distancias] <= 10000 and array_distancias[distancias] > 5000:
            print('\033[1;93m'+string+'\033[m')
        elif array_distancias[distancias] <= 5000 and array_distancias[distancias] > 1000:
            print('\033[1;92m'+string+'\033[m')
        else:
            print('\033[1;96m'+string+'\033[m')

def ganhou1():
    print('\033[1;92mAhhhhh moleque! Parabéns! A vida tá fácil, hein?!\033[m')

def jogar_novamente():
    print('\033[1;35mTá afim de procrastinar mais um pouco? Quer mais uma rodada?[s/n]\033[m')

def digite_s_ou_n():
    print('\033[1;35mEEEEE cabeção! É apenas s ou n\033[m')

def produtivo():
    print('\033[1;35mÉ isso aí, bora ser produtivo! Até mais e bom final de semana!!\033[m')

def erro_digito_opcao_dicas():
    print('\033[1;35mEpa! Essa não é uma das opções válidas! Presta atenção!\033[m')

def display_dicas_ja_foram(dic_dicas):
    for ea in dic_dicas.values():
        print('\033[1;35m'+str(ea)+'\033[m')

def advinha_pais():
    print('\033[1;35mUm país foi sorteado, tente advinhar qual é!\033[m')