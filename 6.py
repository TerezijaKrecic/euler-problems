# Vsota kvadratov prvih 10naravnih števil je 1^2 + 2^2 + 3^2 + ... + 10^2 = 385
# Kvadrat vsote prvih 10 naravnih števil je (1+2+3+...+10)^2 = 3025
# Razlika teh dveh rezultatov je 3025 - 385 = 2640
# Poišči to razliko pri vsoti prvih 100 naravnih števil (raazliko med vsoto kvadratov in kvadratom vsote)

def razlika(n):
    """Poišče razliko med vsoto kvadratov prvih n števil in kvadratom vsote prvih n števil"""
    vsota_kvadratov = 0
    kvadrat_vsote = 0
    for i in range (n + 1):
        vsota_kvadratov += i ** 2
        kvadrat_vsote += i
    return abs(kvadrat_vsote ** 2 - vsota_kvadratov)

print(razlika(100))