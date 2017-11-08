

# coding=utf-8

with open('Alunos.txt') as arquivo:
    for linha in arquivo:
        lista = linha.split(";")
        media = float(lista[1]) + float(lista[2])
        with open('saida.txt', 'w') as arquivo2:
            varLinha = str("{};{}".format(linha,media))
            arquivo2.write(varLinha)