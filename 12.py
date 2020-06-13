# def ali_je_trikotnisko_stevilo(n):
#     vsota = 0
#     for i in range(1, n):
#         if vsota == n:
#             return True
#         else:
#             vsota += i
#     return False

# def faktorji(n):
#     seznam = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             seznam += [i]
#     return seznam

# n = 1
# while len(faktorji(n)) <= 5:
#     n += 1
#     while ali_je_trikotnisko_stevilo(n) != True:
#         n += 1
#print(n)
    
#rabi kakšno minutko ... ali pet ...

def seznam(n):
    trikotniska_stevila = [1]
    for i in range(2, n + 1):
        trikotniska_stevila.append(trikotniska_stevila[i - 2]+ i)
    return trikotniska_stevila

def naslednje_trik_st_od(n):
    

def stevilo_faktorjev_trik_st(n):
    if n not in seznam(n):
        return 0
    vsota = 0
    for i in range(1, n + 1):
        if n % i == 0:
            vsota += 1
    return vsota

def prvo_z_n_delitelji(n):
    i = 1
    while stevilo_faktorjev_trik_st(i) != n



# def delitelji_n_tega_trik_st(n):
#     trikotniska_stevila = {1: 1}
#     for i in range(2, n + 1):
#         trikotniska_stevila[i] = trikotniska_stevila[i - 1] + i
#     stevilo = trikotniska_stevila[n]
#     seznam = []
#     for i in range(1, stevilo + 1):
#         if stevilo % i == 0:
#             seznam += [i]
#     return seznam