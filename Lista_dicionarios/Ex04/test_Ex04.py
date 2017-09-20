from Ex04 import entrada_produtos

def test_entrada_produtos() :
    assert entrada_produtos('cenoura', 10) == ('cenoura':[10,2.1])
    assert entrada_produtos('tomate', 20) == ('tomate':[20,2.3])
    assert entrada_produtos('fim', 0) == -1
    assert entrada_produtos('beterraba', 0) == None