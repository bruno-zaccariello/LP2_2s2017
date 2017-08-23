# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# F. make_tags
# make_tags('i', 'Yay'), '<i>Yay</i>'
# make_tags('i', 'Hello'), '<i>Hello</i>'
# make_tags('cite', 'Yay'), '<cite>Yay</cite>'
def make_tags(tab, word):
  return 

def test_ex06():
  print ('Make Tags')
  assert make_tags('i', 'Yay') == '<i>Yay</i>'
  assert make_tags('i', 'Hello') == '<i>Hello</i>'
  assert make_tags('cite', 'Yay') == '<cite>Yay</cite>'
  assert make_tags('address', 'here') == '<address>here</address>'
  assert make_tags('body', 'Heart') == '<body>Heart</body>'
  assert make_tags('i', 'i') == '<i>i</i>'
  assert make_tags('i', '') == '<i></i>'

