class Aluno():
	def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir

    def Estudar(self, HorasEstudo):
        estudo = HorasEstudo + self.tempoSemDormir
        return estudo

    def Dormir(self, HorasSono):
        dormir = self.tempoSemDormir - HorasSono
        return dormir