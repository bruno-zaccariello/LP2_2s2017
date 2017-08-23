# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# I. sem_pontas
# seja uma string s de pelo menos dois caracteres
# retorna uma string sem o primeiro e último caracter
# sem_pontas('Hello') -> 'ell'
# sem_pontas('python') -> 'ytho'
# sem_pontas('coding') -> 'odin'
def sem_pontas(s):
  return 

def test_ex09():
  print ('Sem Pontas')
  assert sem_pontas('Hello') == 'ell'
  assert sem_pontas('Python') == 'ytho'
  assert sem_pontas('coding') == 'odin'
  assert sem_pontas('code') == 'od'
  assert sem_pontas('ab') == ''
  assert sem_pontas('Chocolate!') == 'hocolate'
  assert sem_pontas('kitten') == 'itte'
  assert sem_pontas('woohoo') == 'ooho'


