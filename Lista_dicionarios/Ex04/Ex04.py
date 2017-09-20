produtos = {
    'tomate':[100, 2.3],
    'alface':[500, 0.45],
    'laranja':[100, 1.3],
    'cenoura':[130, 2.1],
    'manga':[75, 3.45],
}

tupla_produtos = tuple(produtos.keys())

def entrada_produtos():
    nome_produto = input('nome do produto: ')
    if nome_produto == 'fim':
        return -1
    elif nome_produto not in tupla_produtos:
        return None
    else:
        qtd = int(input('Quantidade: '))
        produto = produtos[nome_produto]
        dic_retorno = {nome_produto: [qtd, produto[1]] }
        return dic_retorno

if __name__ == "__main__":
    retorno = 0
    lista_compra = []
    while retorno != -1 :
        nome_produto = input('nome do produto: ')
        if nome_produto != 'fim' :
            qtd = int(input('Quantidade: '))
        retorno = entrada_produtos()
        if retorno != -1 and retorno != None:
            lista_compra.append(retorno)
    print(lista_compra)