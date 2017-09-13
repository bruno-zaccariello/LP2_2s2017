from Ex01 import MDC

def test_ex01():
    assert MDC(10, 15) == 5
    assert MDC(20, 30) == 10
    assert MDC(45, 450) == 45
    assert MDC(12, 18) == 6