def pego_correndo(speed, is_birthday):
	retorno = 0
	if is_birthday == True:
		if speed <= 65:
			retorno = 0
		elif 65 < speed <= 85	:
			retorno = 1
		elif speed > 85	:
			retorno = 2
	elif is_birthday == False:
		if speed <= 60	:
			retorno = 0
		elif 60 < speed <= 80	:
			retorno = 1
		elif speed > 80	:
			retorno = 2
	return retorno