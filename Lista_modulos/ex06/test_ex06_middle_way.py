# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# F. middle_way
# sejam duas listas de inteiros a e b
# retorna uma lista de tamanho 2 contendo os elementos do
# meio de a e b, suponha que as listas tem tamanho ímpar
# middle_way([1, 2, 3], [4, 5, 6]) -> [2, 5]
# middle_way([7, 7, 7], [3, 8, 0]) -> [7, 8]
# middle_way([5, 2, 9], [1, 4, 5]) -> [2, 4]

from ex06 import middle_way

def test_ex06():
  print ('middle_way')
  assert middle_way([1, 2, 3], [4, 5, 6]) == [2, 5]
  assert middle_way([7, 7, 7], [3, 8, 0]) == [7, 8]
  assert middle_way([5, 2, 9], [1, 4, 5]) == [2, 4]
  assert middle_way([1, 9, 7], [4, 8, 8]) == [9, 8]
  assert middle_way([1, 2, 3], [3, 1, 4]) == [2, 1]
  assert middle_way([1, 2, 3], [4, 1, 1]) == [2, 1]

