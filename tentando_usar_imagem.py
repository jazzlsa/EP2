# Lendo de linha em linha (note o plural em readlines)
with open('rapozinha.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    arquivo.close()

raposinha = []
for linha in linhas:
    raposinha.append(linha)
for li in raposinha:
    print('\033[1;35m'+str(li)+'\033[m', end='')

'''
print('\033[1;30;45m  ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀ ✿ ❀   \033[m')
    print('\033[1;30;45m ☺                                ☺ \033[m')
    print('\033[1;30;45m ☺   Bem-vindo ao Insper Países   ☺ \033[m')
    print('\033[1;30;45m ☺                                ☺ \033[m')
    print('\033[1;30;45m  ✿ ❀ ✿ Design de Software✿ ❀ ✿ ❀   \033[m')
'''