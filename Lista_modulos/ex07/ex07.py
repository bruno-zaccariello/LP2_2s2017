def date_fashion(eu, par):
  if eu <= 2 or par <= 2 :
    return 0
  elif eu >= 8 and 2 < par :
    return 2
  elif par >= 8 and 2 < eu :
    return 2
  elif 2 < eu < 8 and 2 < par < 8 :
    return 1