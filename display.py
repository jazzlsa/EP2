#funções de tela
from zmq import NULL


def display_boas_vindas():
    print('')
    print(' ✿❀✿❀✿❀✿❀✿❀✿❀✿❀✿❀✿❀✿❀ ')
    print('☺                                ☺')
    print('☺   Bem-vindo ao Insper Países   ☺')
    print('☺                                ☺')
    print(' ❀✿❀✿❀Design de Software✿❀✿❀ ')
    print('')

def display_menu():
    print('')
    print('Comandos:')
    print('dica       - Entra no mercado de dicas')
    print('desisto    - Desiste da rodada')
    print('inventario - Exibe sua posição')
    print('menu       - Exibe este menu')
    print('')
    
def display_mercado_dicas(dicas_permitidas):
    string_opcoes=''
    outras_opcoes = False
    print('')
    print('Mercado de Dicas')
    print('----------------------------------------')
    if(dicas_permitidas['1']):
        print('1. Cor da bandeira  - custa 4 tentativas')
        string_opcoes=string_opcoes+'|1'
    if(dicas_permitidas['2']):
        print('2. Letra da capital - custa 3 tentativas')
        string_opcoes=string_opcoes+'|2'
    if(dicas_permitidas['3']):
        print('3. Área             - custa 6 tentativas')
        string_opcoes=string_opcoes+'|3'
    if(dicas_permitidas['4']):
        print('4. População        - custa 5 tentativas')
        string_opcoes=string_opcoes+'|4'
    if(dicas_permitidas['5']):
        string_opcoes=string_opcoes+'|5'
    print('0. Voltar')
    print('----------------------------------------')
    entrada_dicas = input('Escolha sua opção [0'+string_opcoes+']:')
    return entrada_dicas

def display_tentativas_restantes(tentativas):
    print('')
    print('Você possui '+str(tentativas)+' restantes')
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