from Ex02 import cont_vogais

def test_Ex02():
    assert cont_vogais('laranja') == {'a':3, 'e':0, 'i':0, 'o':0, 'u':0}
    assert cont_vogais('exercicio dois') == {'a':0, 'e':2, 'i':3, 'o':2, 'u':0}
    assert cont_vogais('sopa de feijao') == {'a': 2, 'e': 2, 'i': 1, 'o': 2, 'u': 0}