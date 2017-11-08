class Livro():
	def __init__(self, nome, qtdPaginas, autor, preco):
        self.nome = nome
        self.qtdPaginas = qtdPaginas
        self.autor = autor
        self.preco = preco

    def getPreco(self):
        return self.preco

    def setPreco(self, novoPreco):
        self.preco = novoPreco