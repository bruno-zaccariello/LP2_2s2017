contatos = {}
opcoes = [1, 2, 3, 4]
opt = 1
while opt in opcoes:
    opt = int(input("Insira a opcao desejada:\n1 - Inserir\n2 - Remover\n3 - Pesquisar\n4 - Sair\n"))
    if opt == 1:
        nome = input("Insira o nome\n")
        if nome in contatos.keys():
            print("Contato existente, atualizar dados\n")
        email = input("Insira o email\n")
        telefone = input("Insira o telefone\n")
        endereco = input("Insira o endereço\n")
        contatos[nome] = [email,telefone,endereco]
    elif opt == 2:
        nome = input("Nome do contato a remover\n")
        while nome not in contatos.keys():
            print("Usuario não encontrado")
            nome = input("Nome do contato a remover\n")
        del contatos[nome]
    elif opt == 3:
        nome = input("Nome do contato a Pesquisar\n")
        if nome in contatos.keys():
            print(contatos[nome])
        else :
            print("Contato não encontrado")
    elif opt == 4:
        print("Programa Encerrado")
        break
if opt not in opcoes:
    print("Opcao Inexistente")