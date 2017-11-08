# coding=utf-8

palavras = {}

with open("tweets.txt") as arquivo :
    conteudo = arquivo.read()
    for palavra in conteudo.split(" "):
        if palavra in palavras:
            palavras[palavra] += 1
        else:
            palavras[palavra] = 1

with open("saida.txt", "w") as arquivo :
    with open("saida.txt", "w") as arquivo2 :
        for item in palavras.items():
            linha = str("{} \n".format(item))
            arquivo2.write(linha)

with open("saida.txt") as arquivo :
    conteudo = arquivo.read()
    print(conteudo)