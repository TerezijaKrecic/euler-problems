# Prvih 6 praštevil: 2, 3, 5, 7, 11, 13.
# Šesto praštevilo je 13.
# Katero je 10001-to praštevilo?

def ali_je_prastevilo(n):
    """preveri, ali je n praštevilo"""
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def n_to_prastevilo(n):
    """ poišče n-to praštevilo"""
    števec = 0
    x = 1
    while števec != n:
        if ali_je_prastevilo(x) == True:
            števec += 1
        x += 1
    return x - 1

print(n_to_prastevilo(10001))
#rabi pol minutke heh:)
        