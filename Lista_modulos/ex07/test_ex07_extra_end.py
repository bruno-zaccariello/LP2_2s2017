# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# G. date_fashion
# você e sua namorada(o) vão a um restaurante
# eu e par são as notas das suas roupas de 0 a 10
# quanto maior a nota mais chique vocês estão vestidos
# o resultado é se vocês conseguiram uma mesa no restaurante:
# 0=não 1=talvez e 2=sim
# se a nota da roupa de um dos dois for menor ou igual a 2
# vocês não terão direito à uma mesa (0)
# se as notas são maiores, então caso um dos dois esteja
# bem chique (nota >= 8) então a resposta é sim (2)
# caso contrário a resposta é talvez (1)
# date_fashion(5, 10) -> 2
# date_fashion(5, 2) -> 0
# date_fashion(5, 5) -> 1

from ex07 import date_fashion

def test_ex07():
  print ('date fashion')
  assert date_fashion(5, 10) == 2
  assert date_fashion(5, 2) == 0
  assert date_fashion(5, 5) == 1
  assert date_fashion(3, 3) == 1
  assert date_fashion(10, 2) == 0
  assert date_fashion(2, 9) == 0
  assert date_fashion(9, 9) == 2
  assert date_fashion(10, 5) == 2
  assert date_fashion(2, 2) == 0
  assert date_fashion(3, 7) == 1
  assert date_fashion(2, 7) == 0
  assert date_fashion(6, 2) == 0

