# pitagorejska trojica je množica 3 naravnih števil a < b < c,
# za katere velja a^2 + b^2 = c^2
# primer: 3^2 + 4^2 = 9 + 16 = 25 = 5^2
# obstaja točno ena trojica, za katero velja a+b+c = 1000
# najdi produkt abc

for a in range(1000):
    for b in range(a + 1, 1000):
        for c in range(b + 1, 1000):
            if a ** 2 + b ** 2 == c ** 2:
                if a + b + c == 1000:
                    print(a * b * c)
