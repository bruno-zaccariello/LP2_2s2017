# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# B. same_first_last
# retorna True se a lista nums possui pelo menos um elemento
# e o primeiro elemento é igual ao último
# same_first_last([1, 2, 3]) -> False
# same_first_last([1, 2, 3, 1]) -> True
# same_first_last([1, 2, 1]) -> True

from ex02 import same_first_last

def test_ex02():
  print ('Same_first_last')
  assert same_first_last([1, 2, 3]) == False
  assert same_first_last([1, 2, 3, 1]) == True
  assert same_first_last([1, 2, 1]) == True
  assert same_first_last([7]) == True
  assert same_first_last([]) == False
  assert same_first_last([7, 7]) == True


