def normaliza(dic):

    saida = {}

    for continente in dic.keys():
        for pais in dic[continente]:
            
            conteudo = dic[continente][pais]
            
            saida[pais] = conteudo
            
    return saida