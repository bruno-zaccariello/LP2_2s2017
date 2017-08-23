# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# B. string_splosion
# string_splosion('Code') -> 'CCoCodCode'
# string_splosion('abc') -> 'aababc'
# string_splosion('ab') -> 'aab'
def string_splosion(s):
  return

def test_ex02():
  print ('String Explosion')
  assert string_splosion('Code') == 'CCoCodCode'
  assert string_splosion('abc') == 'aababc'
  assert string_splosion('ab') == 'aab'
  assert string_splosion('x') == 'x'
  assert string_splosion('fade') == 'ffafadfade'
  assert string_splosion('There') == 'TThTheTherThere'
  assert string_splosion('Kitten') == 'KKiKitKittKitteKitten'
  assert string_splosion('Bye') == 'BByBye'
  assert string_splosion('Good') == 'GGoGooGood'
  assert string_splosion('Bad') == 'BBaBad'
