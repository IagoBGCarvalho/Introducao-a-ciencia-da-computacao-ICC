x = input().strip()
y = input().strip()

if x == y:
    print(-1)
else:
    print(max(len(x), len(y)))
