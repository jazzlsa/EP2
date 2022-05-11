from dados import DADOS
import funcoes

continuar ='s' #inicia continuar

dicas_compradas = [] #inicia dicas compradas

ganhou = false #inicia ganhou

desistiu = false #inicia desistiu

while continuar == 's': # laço para garantir que ele continue jogando até dizer que não
  quantidade_tentativas = 20 #inicia quantidade de tentativas
  dados_normalizados = normaliza(dados.DADOS)
  print(sorteia_pais(dados_normalizados))
  while tentativas!=0:
    


  print('Perdeu! O país era {}')
  continuar=input('Jogar Novamente?s/n ')
  while continuar!='s' and continuar!='n':
    continuar=input('Ops! Não entendi. Digite s/n: ')
