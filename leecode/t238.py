a = [1, 2, 3, 4]
cnt = len(a)
b = [1, 1, 1, 1]
c = [0, 0, 0, 0]


# 0(n*n)
def func1():
    for i in range(0, cnt):
        for j in range(0, cnt):
            if i != j:
                b[i] = b[i] * a[j]
    print(b)


# o(n)
def func2():
    for i in range(0, cnt):
        if i == 0:
            b[i] = a[i]
            continue
        b[i] = b[i - 1] * a[i]

    for i in range(cnt - 1, -1, -1):
        if i == cnt - 1:
            c[i] = a[i]
            continue
        c[i] = c[i + 1] * a[i]

    for i in range(1, cnt - 1):
        c[i] = b[i - 1] * c[i + 1]
    c[cnt - 1] = b[cnt - 2]
    print(c)


# 少用空间，只用一个数组
def func3():
    for i in range(0, cnt):
        if i == 0:
            b[i] = a[i]
            continue
        b[i] = b[i - 1] * a[i]

    tmp = 1
    for i in range(cnt - 1, -1, -1):
        if i == cnt - 1:
            b[i] = b[i - 1]
        else:
            b[i] = b[i - 1] * tmp
        tmp = tmp * a[i]
    b[0] = tmp
    print(b)


func3()
