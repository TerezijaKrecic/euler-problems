#iščemo najm. poz. število, ki ga delijo vsa števila od 1 do vklj. 20 - BREZ OSTANKA!!
# torej iščemo najmanjši skupni večkratnik števil \in [1, 20]

def najm_sk_večkratnik(a, b):
    """najmanjši skupni večkratnik 2 števil"""
    for i in range(max(a, b), a * b + 1):
        if i % a == 0 and i % b == 0:
            return i
            break

def fakulteta(n):
    if n < 2:
        return 1
    else:
        return n * fakulteta(n - 1)

def najmanjsi_veckratnik(n):
    """najm.sk.večkratnik števil od 1 do vklučno n"""
    for i in range(n, fakulteta(n) + 1):
        a = 0
        for j in range(1, n + 1):
            if i % j == 0:
                a += 1
        if a == n:
            return i

#)print(najmanjsi_veckratnik(20))

def večkratnik(seznam):
    """Poišče najmanjši skupni večkratnik števil iz seznama"""
    if seznam == []:
        return 0
    elif len(seznam) == 1:
        return seznam[0]
    else:
        seznam[1] = najm_sk_večkratnik(seznam[0], seznam[1])
        return večkratnik(seznam[1:])

#print(večkratnik([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))