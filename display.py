#funções de tela
import funcoes
from zmq import NULL


def display_boas_vindas():
    print('')
    print('\033[1;30;45m  ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀   \033[m')
    print('\033[1;30;45m ☺                                ☺ \033[m')
    print('\033[1;30;45m ☺   Bem-vindo ao Insper Países   ☺ \033[m')
    print('\033[1;30;45m ☺                                ☺ \033[m')
    print('\033[1;30;45m  ✿ ❀ ✿ Design de Software✿ ❀ ✿ ❀   \033[m')
    print('')

def display_menu():
    print('')
    print('\033[1;30;45mComandos:                                     \033[m')
    print('\033[1;30;45mdica       - Entra no mercado de dicas\033[m')
    print('\033[1;30;45mdesisto    - Desiste da rodada        \033[m')
    print('\033[1;30;45minventario - Exibe sua posição        \033[m')
    print('\033[1;30;45mmenu       - Exibe este menu                             \033[m')
    print('')
    
def display_mercado_dicas(dicas_permitidas):
    string_opcoes=''
    outras_opcoes = False
    print('')
    print('\033[1;30;45mMercado de Dicas                            \033[m')
    print('\033[1;30;45m✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀\033[m')
    if(dicas_permitidas['1']):
        print('\033[1;30;45m1. Cor da bandeira  - custa 4 tentativas\033[m')
        string_opcoes=string_opcoes+'|1'
    if(dicas_permitidas['2']):
        print('\033[1;30;45m2. Letra da capital - custa 3 tentativas\033[m')
        string_opcoes=string_opcoes+'|2'
    if(dicas_permitidas['3']):
        print('\033[1;30;45m3. Área             - custa 6 tentativas\033[m')
        string_opcoes=string_opcoes+'|3'
    if(dicas_permitidas['4']):
        print('\033[1;30;45m4. População        - custa 5 tentativas\033[m')
        string_opcoes=string_opcoes+'|4'
    if(dicas_permitidas['5']):
        string_opcoes=string_opcoes+'|5'
    print('\033[1;30;45m0. Voltar                                     \033[m')
    print('\033[1;30;45m✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀\033[m')
    entrada_dicas = input('Escolha sua opção [0'+string_opcoes+']:')
    return entrada_dicas

def display_tentativas_restantes(tentativas):
    print('')
    if tentativas > 10:
        print('Você possui \033[1;32m'+str(tentativas)+'\033[m restantes')
    else: 
        if tentativas <= 10 and tentativas > 5:
            print('Você possui \033[1;33m'+str(tentativas)+'\033[m restantes')
        else:
            print('Você possui \033[1;31m'+str(tentativas)+'\033[m restantes')
    print('')

def display_confirma_desisto():
    print('')
    print('Não acredito que você seja um arregão. Quer mesmo desistir?')
    print('[s/n]')

def display_nao_desisto():
    print('')
    print('Sabia que você não era um arregão!')
    print('')

def display_sim_desisto():
    print('')
    print('Sabia que você era um arregão!')
    print('')

def display_distancias(array_distancias):
    for linhas in array_distancias:
        print(array_distancias[linhas])

def ganhou1():
    print('Ahhhhh moleque! Parabéns! A vida tá fácil, hein?!')

def jogar_novamente():
    print('Tá afim de procrastinar mais um pouco? Quer mais uma rodada?[s/n]')

def digite_s_ou_n():
    print('EEEEE cabeção! É apenas s ou n')

def produtivo():
    print('É isso aí, bora ser produtivo! Até mais e bom final de semana!!')

def erro_digito_opcao_dicas():
    print('Epa! Essa não é uma das opções válidas! Presta atenção!')