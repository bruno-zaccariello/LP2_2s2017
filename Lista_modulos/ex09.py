def pego_correndo(speed, is_birthday):
  if is_birthday == True :
    if speed <= 65 :
	  return 0
	elif 65 < speed <= 85 :
	  return 1
	elif speed > 85 :
	  return 2
  if is_birthday == False :
    if speed <= 60 :
	  return 0
	elif 60 < speed <= 80 :
	  return 1
	elif speed > 80 :
	  return 2