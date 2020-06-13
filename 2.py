def manjsa_od(n):
    """Sešteje soda fib.števila, ki niso večja od 4miljonov"""
    a = 1
    b = 2
    vsota = b
    seznam = [a, b]
    while a + b <= n:
        seznam += [a + b]
        if (a + b) % 2 == 0:
            vsota += (a + b)
        x = a
        a = b
        b = x + b #tu a dobi vrednost b-ja, b pa vrednost vsote a + b
    print(seznam) #to je seznam fib.števil od 1, 2, do števila, ki še ne presega 4miljone)
    print(vsota)
manjsa_od(4000000)
#seznama ni treba delat, amak se potem lažje vidi ...)