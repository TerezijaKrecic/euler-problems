def ali_je_palindrom(n):
    """preveri, ali je število n palindrom"""
    n = str(n)
    if n == '' or len(n) == 1:
        return True
    elif n[0] == n[-1]:
        return ali_je_palindrom(n[1:-1])
    else:
        return False

# iščemo največje število, ki je palindrom in je produkt dveh tromestnih števil
def produkt_do():
    """Gre skozi vse možne produkte 3-mestnih števil in izpiše največjega"""
    a = 0
    for i in range (100, 1000):
        for j in range (100, 1000):
            if ali_je_palindrom(i * j) == True:
                a = max(a, i * j)
    return a

print(produkt_do()) #za argument lahko daš karkoli, ker ne vpliva na nič


#nepotrebna funkcija, ki poišče največji el. seznama
#def najv_el_seznama(seznam):
#    if seznam == []:
#        return 0
#    else:
#        return max(seznam[0], najv_el_seznama(seznam[1:]))