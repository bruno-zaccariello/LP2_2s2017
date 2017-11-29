from cadastro import Cadastro

opc = int(input("Escolha sua opção:\n1 - Cadastro\n2 - Boletim\n3 - Matricula")):
if opc == 1 :
    opc2 = int(input("O que você deseja cadastrar:\n1 - Aluno\n2 - Professor\n3 - Curso\n4 - Disciplina")):
    if opc2 == 1 :
        Cadastro.aluno()