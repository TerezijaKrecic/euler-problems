def sestej(n):
    """Sešteje vse večkratnike 3 in 5 do nekega števila (brez tega števila)"""
    vsota = 0
    for i in range(3, n):
        if i % 3 == 0 or i % 5 == 0:
            vsota += i
    print(vsota)

sestej(1000)