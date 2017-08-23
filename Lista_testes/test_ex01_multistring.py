# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# A. multstring
# seja uma string s e um inteiro positivo n
# retorna uma string com n cópias da string original
# multstring('Hi', 2) -> 'HiHi'
def multstring(s, n):
  return

def test_ex01():
  print ('Multstring')
  assert multstring('Hi', 2) == 'HiHi'
  assert multstring('Hi', 3) == 'HiHiHi'
  assert multstring('Hi', 1) == 'Hi'
  assert multstring('Hi', 0) == ''
  assert multstring('Hi', 5) == 'HiHiHiHiHi'
  assert multstring('Oh Boy!', 2) == 'Oh Boy!Oh Boy!'
  assert multstring('x', 4) == 'xxxx'
  assert multstring('', 4) == ''
  assert multstring('code', 2) == 'codecode'
  assert multstring('code', 3) == 'codecodecode'


