# coding=utf-8

with open('Alunos.txt') as arquivo:
    for linha in arquivo:
        lista = linha.split(";")
        media = (float(lista[1]) + float(lista[2]))/2
        with open('saida.txt', 'a') as arquivo2:
            newLinha = str("%s;%s\n" %(linha, media))
            varLinha = str("{};{}\n".format(linha,media))
            arquivo2.write(newLinha)