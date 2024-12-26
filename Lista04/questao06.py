def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def mmc(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

while True:
    entrada = input()
    a, b = map(int, entrada.split())
    if a < 0 or b < 0:
        break
    print(mmc(a, b))