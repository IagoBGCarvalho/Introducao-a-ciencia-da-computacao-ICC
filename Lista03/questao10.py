def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())

m = 1
while True:
    if not is_prime(n * m + 1):
        print(m)
        break
    m += 1
