a = 10
b = 10


def dodaj():
    a = 6
    b = 7
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a
    a = 8
    b = 8
    print(a + b)


print("zmienna a z góry", a)
dodaj()
print("zmienna a z góry", a)
dodaj2()
print("zmienna a z góry", a)
dodaj3()
print("zmienna a z góry", a)  # zmienna a z góry 8
dodaj2()
print("zmienna a z góry", a)
