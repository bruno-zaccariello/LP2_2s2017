# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# E. sum2
# Dada uma lista de inteiros de qualquer tamanho
# retorna a soma dos dois primeiros elementos
# se a lista tiver menos de dois elementos, soma o que for possível

from ex05 import sum2

ex05.sum2()

def test_ex05():
  print ('sum2')
  assert sum2([1, 2, 3]) == 3
  assert sum2([1, 1]) == 2
  assert sum2([1, 1, 1, 1]) == 2
  assert sum2([1, 2]) == 3
  assert sum2([1]) == 1
  assert sum2([]) == 0
  assert sum2([4, 5, 6]) == 9
  assert sum2([4]) == 4

