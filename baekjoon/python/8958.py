n = int(input())
for i in range(n):
    sc = 0
    sc_s = 0
    ox = input()
    for j in ox:
        if j == 'O':
            sc += 1
        else:
            sc = 0
        sc_s += sc
    print(sc_s)
