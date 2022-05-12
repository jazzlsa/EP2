#funções de tela
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
    
def display_mercado_dicas():
    print('')
    print('Mercado de Dicas')
    print('----------------------------------------')
    print('1. Cor da bandeira  - custa 4 tentativas')
    print('2. Letra da capital - custa 3 tentativas')
    print('3. Área             - custa 6 tentativas')
    print('4. População        - custa 5 tentativas')
    print('5. Continente       - custa 7 tentativas')
    print('0. Sem dica')
    print('----------------------------------------')
    #necessário alterar depois
    print('Escolha sua opção [0|1|2|3|4|5]:')
    print('')

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
        print(linhas)

def nao_ganhou():
    print('Ihhh! Não foi dessa vez, meu chapa! O país era '+pais_sorteado['nome']+', fechou?')

def ganhou1():
    print('Ahhhhh moleque! Parabéns! A vida tá fácil, hein?!')

def jogar_novamente():
    print('Tá afim de procastinar mais um pouco? Quer mais uma rodada?[s/n]')

def digite_s_ou_n():
    print('EEEEE cabeção! É apenas s ou n')

def produtivo():
    print('É isso aí, bora ser produtivo! Até mais e bom final de semana!!')

