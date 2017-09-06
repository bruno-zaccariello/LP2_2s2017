# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# C. common_end
# Dada duas listas a e b verifica se os dois primeiros são
# iguais ou os dois últimos são iguais
# suponha que as listas tenham pelo menos um elemento
# common_end([1, 2, 3], [7, 3]) -> True
# common_end([1, 2, 3], [7, 3, 2]) -> False
# common_end([1, 2, 3], [1, 3]) -> True

from ex03 import common_end


def test_ex03():
  print ('Common_end')
  assert common_end([1, 2, 3], [7, 3]) == True
  assert common_end([1, 2, 3], [7, 3, 2]) == False
  assert common_end([1, 2, 3], [1, 3]) == True
  assert common_end([1, 2, 3], [1]) == True
  assert common_end([1, 2, 3], [2]) == False


