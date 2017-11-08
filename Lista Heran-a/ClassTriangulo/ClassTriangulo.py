class Triangulo():
	def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def perimetro(self):
        per = self.ladoA + self.ladoB + self.ladoC
        return per

    def getMaior(self):
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC :
			ml = self.ladoA
		elif self.ladoB > self.ladoA and self.ladoB > self.ladoC :
			ml = self.ladoB
		elif self.ladoC > self.ladoB and self.ladoC > self.ladoA :
			ml = self.ladoB
        return ml