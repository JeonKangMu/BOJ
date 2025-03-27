a, b = map(int, input().split())

if (a - b) > b or (a <= b):
    print("NO")
else:
    print("YES")
    print(a - b)
    if a == 2*b:
        print("aba")
    else:
        print("a", end="")
        for i in range(b - (a - b) + 1):
            print("ba", end="")
        print()
    for i in range(a - b - 1):
        print("aba")