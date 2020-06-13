def ali_je_prastevilo(n):
    """preveri, ali je n praštevilo"""
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def najvecji_prafaktor(n):
    """poišče največji prafaktor števila n"""
    a = 2
    while a <= n:
        if ali_je_prastevilo(a) == True:
            if n % a == 0:
                n //= a
            else:
                a += 1
        else:
            a += 1
    return a

print(najvecji_prafaktor(600851475143))