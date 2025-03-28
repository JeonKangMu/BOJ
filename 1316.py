import sys

n = int(sys.stdin.readline())
cnt = 0;
for _ in range(n):
    a = sys.stdin.readline().strip()
    word = list(a)
    check = []
    flag = 0;

    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            continue
        check.append(word[i])
    check.append(word[-1])

    for j in check:
        if check.count(j) > 1:
            flag = 1
            break

    if flag == 0:
        cnt += 1
print(cnt)