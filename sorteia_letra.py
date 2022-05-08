import random

def sorteia_letra(palavra, lista_restrita):

    especiais = ['.', ',', '-', ';', ' ', '@', '!', '$', '%', '*', '(', ')', '{', '}', '[', ']', ':']
    saida = ''
    palavra = palavra.lower()
    palavra_lista = []

    continua = False

    for letra in palavra:
        palavra_lista.append(letra)

        if letra not in especiais and letra not in lista_restrita:
            continua = True

    while continua:

        saida = random.choice(palavra_lista)
        
        if saida in especiais or saida in lista_restrita:
            while saida in especiais or saida in lista_restrita:
                saida = random.choice(palavra_lista)
            
        continua = False

    return saida