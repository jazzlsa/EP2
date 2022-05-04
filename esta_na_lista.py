def esta_na_lista(pais, listas):

    tem = False

    for lista in listas:
        if pais in lista:
            tem = True

    return tem