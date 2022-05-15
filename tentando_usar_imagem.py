# Lendo de linha em linha (note o plural em readlines)
with open('rapozinha.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    arquivo.close()

raposinha = []
for linha in linhas:
    raposinha.append(linha)
for li in raposinha:
    print('\033[1;31m'+str(li)+'\033[m', end='')


