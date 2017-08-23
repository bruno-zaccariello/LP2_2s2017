# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# H. first_half
# seja uma string s
# retorna a primeira metade da string
# first_half('WooHoo') -> 'Woo'
# first_half('HelloThere') -> 'Hello'
# first_half('abcdef') -> 'abc'
def first_half(s):
  return 


def test_ex08():
  print ('First Half')
  assert first_half('WooHoo') == 'Woo'
  assert first_half('HelloThere') == 'Hello'
  assert first_half('abcdef') == 'abc'
  assert first_half('ab') == 'a'
  assert first_half('') == ''
  assert first_half('0123456789') == '01234'
  assert first_half('kitten') == 'kit'


