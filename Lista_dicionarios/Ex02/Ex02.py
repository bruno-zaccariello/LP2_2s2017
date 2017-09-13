def cont_vogais(texto) :
    vogais = ['a','e','i','o','u']
    dic = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    for letra in texto:
        if letra == 'a':
            dic['a'] += 1
        elif letra == 'e':
            dic['e'] += 1
        elif letra == 'i':
            dic['i'] += 1
        elif letra == 'o':
            dic['o'] += 1
        elif letra == 'u':
            dic['u'] += 1
    return dic