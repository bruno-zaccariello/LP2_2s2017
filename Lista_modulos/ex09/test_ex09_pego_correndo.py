# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# I. pego_correndo
# você foi pego correndo
# o resultado será:
# sem multa = 0
# multa média = 1
# multa grave = 2
# velocide <= 60 sem multa
# velocidade entre 61 e 80 multa média
# velocidade maior que 81 multa grave (cidade do interior)
# caso seja seu aniversário a velocidade pode ser 5 km/h maior em todos os casos
# pego_correndo(60, False) -> 0
# pego_correndo(65, False) -> 1
# pego_correndo(65, True) -> 0 

from ex09 import pego_correndo
 
def test_ex09():
  print ('Pego correndo')
  assert pego_correndo(60, False) == 0
  assert pego_correndo(65, False) == 1
  assert pego_correndo(65, True) == 0
  assert pego_correndo(80, False) == 1
  assert pego_correndo(85, False) == 2
  assert pego_correndo(85, True) == 1
  assert pego_correndo(70, False) == 1
  assert pego_correndo(75, False) == 1
  assert pego_correndo(75, True) == 1
  assert pego_correndo(40, False) == 0
  assert pego_correndo(40, True) == 0
  assert pego_correndo(90, False) == 2

 
