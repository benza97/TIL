if __name__ == '__main__':
    n = int(input('hi'))
    i = 1
    x = str(1)
    if n == 1:
        print(n)
    elif n > 1:
        while n > 1:
            i += 1
            x = str(x) + str(i)
        print(x)