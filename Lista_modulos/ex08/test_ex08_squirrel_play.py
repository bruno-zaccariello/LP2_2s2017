# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# H. squirrel_play
# os esquilos na FIT brincam quando a temperatura está entre 60 e 90
# graus Fahreneit (são estrangeiros e o termômetro é diferente rs)
# A menos que seja verão, então a temperatura limite é 100 ao invés de 90
# retorne True caso os esquilos brinquem
# squirrel_play(70, False) -> True
# squirrel_play(95, False) -> False
# squirrel_play(95, True) -> True

from ex08 import squirrel_play

def test_ex08():
  print ('squirrel_play')
  assert squirrel_play(70, False) == True
  assert squirrel_play(95, False) == False
  assert squirrel_play(95, True) == True
  assert squirrel_play(90, False) == True
  assert squirrel_play(90, True) == True
  assert squirrel_play(50, False) == False
  assert squirrel_play(50, True) == False
  assert squirrel_play(100, False) == False
  assert squirrel_play(100, True) == True
  assert squirrel_play(105, True) == False
  assert squirrel_play(59, False) == False
  assert squirrel_play(59, True) == False	
  assert squirrel_play(60, False) == True
 
