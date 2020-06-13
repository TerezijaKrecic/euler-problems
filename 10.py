# vsota praštevil pod 10 je 2+3+5+7 = 17.
# poišči vsoto praštevil pod 2 milijona

def ali_je_prastevilo(n):
    """preveri, ali je n praštevilo"""
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


#prastevila = {i for i in range(2000000) if ali_je_prastevilo(i)}
#print(sum(prastevila))

vsota = {2}
for i in range(3, 2000000):
    if ali_je_prastevilo(i):
        vsota.add(i)
print(sum(vsota))
#nekaj časa melje ... in ne pride do konca ...

# vsota praštevil do 50.000 je 121013308
# vsota praštevil med 50.000 in 80.000 je 175474900
# med 80.000 in 110.000 je 248326848