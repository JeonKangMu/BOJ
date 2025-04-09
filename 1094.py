x = int(input())

lens = [64, 32, 16, 8, 4, 2, 1]

cnt = 1;
for i in lens:
    if i > x:
        continue

    if i == x:
        break

    x -= i
    cnt += 1

print(cnt)