def alarm_clock(day, vacation):
  if day in range (1,5) :
    if vacation == True :
      return '10:00'
    elif vacation == False :
      return '7:00'
  elif day == 0 or day == 6 :
    if vacation == True :
      return 'off'
    elif vacation == False :
      return '10:00'
  return