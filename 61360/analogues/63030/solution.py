for x in range(40):
    for y in range(40):
        t = 5 * 40 ** 8 + 7 * 40 ** 7 + x * 40 ** 6 + 6 * 40 ** 5 + 9 * 40 ** 4 + 2 * 40 ** 3 + y * 40 ** 2 + 1 * 40 + 9

        n = y * 40 + x
        root = int(n ** 0.5)

        if t % 39 == 0 and root * root == n:
            print(n)
