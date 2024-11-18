a, b = map(int, input().split())

if a == 0 and b == 0:
    print(f"{a} {b} errados")
elif b >= a and b - a <= 1:
    print(f"{a} {b} ok")
else:
    print(f"{a} {b} errados")
