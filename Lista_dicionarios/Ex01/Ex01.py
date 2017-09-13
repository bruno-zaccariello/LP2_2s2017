def MDC(a, b) :
    while (b != 0) :
        q = a / b
        r = a % b
        a = b
        b = r
    return a