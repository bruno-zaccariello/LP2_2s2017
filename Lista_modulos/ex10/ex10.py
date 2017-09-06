def alarm_clock(day, vacation):
  retorno = 'off'
  if 0 < day <= 5 :
    if vacation == True :
      retorno = '10:00'
    elif vacation == False :
      retorno = '7:00'
  elif day == 0 or day == 6 :
    if vacation == True :
      retorno = 'off'
    elif vacation == False :
      retorno = '10:00'
  return retorno