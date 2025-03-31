while True:

    try:
        n = int(input())
        if not n:
            break

        idx = 1
        sol = 1

        while True:
            if sol % n == 0:
                print(idx)
                break
            else:
                sol = sol * 10 + 1
                idx += 1

    except EOFError:
        break