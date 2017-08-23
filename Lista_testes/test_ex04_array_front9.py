# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# D. array_front9
# verifica se pelo menos um dos quatro primeiros é nove
# array_front9([1, 2, 9, 3, 4]) -> True
# array_front9([1, 2, 3, 4, 9]) -> False
# array_front9([1, 2, 3, 4, 5]) -> False
def array_front9(nums):
  return

def test_ex04():
  print ('Array front 9')
  assert array_front9([1, 2, 9, 3, 4]) == True
  assert array_front9([1, 2, 3, 4, 9]) == False
  assert array_front9([1, 2, 3, 4, 5]) == False
  assert array_front9([9, 2, 3]) == True
  assert array_front9([1, 9, 9]) == True
  assert array_front9([1, 2, 3]) == False
  assert array_front9([1, 9]) == True
  assert array_front9([5, 5]) == False
  assert array_front9([2]) == False
  assert array_front9([9]) == True
  assert array_front9([]) == False
  assert array_front9([3, 9, 2, 3, 3]) == True

