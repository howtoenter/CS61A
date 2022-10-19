def double_eights(n):
    while True:
        if n % 100 == 88:
            print(True)
            break
        else:
            n = n // 10
        if n // 10 == 0:
            print(False)
            break
