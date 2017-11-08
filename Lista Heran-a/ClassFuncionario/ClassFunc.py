class Funcionario():
	def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentarSalario(self, percent):
        self.salario = (self.salario * (1 + (percent / 100)))
        return self.salario


