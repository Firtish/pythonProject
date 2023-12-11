# funkcja - wydzielony fragment kodu który można użyć wielokrotnie
a = 8
b = 9


# deklaracja funkjci
def dodaj():
    c = 7  # zmienna lokalna
    print(a + b)


def dodaj2(a, b):  # a i b są lokalne obowiązkowo muszą być przekazane parametry
    print(a + b)


# można zasymulować przeciążenie argumentów funkcji poprzez wartość domyślną
def odejmij(a, b, c=0):  # c - parametr domyślny
    print(a - b - c)


dodaj()  # 17
# print(c)
dodaj2(5, 6)  # 11
odejmij(1, 2)
odejmij(1, 2, 3)  # argumenty pozycyjne
odejmij(b=7, c=7, a=9)  # argumenty przekazane po nazwie

print(dodaj())  # None
# TypeError: unsupported operand type(s) for -: 'NoneType' and 'NoneType'
# print(odejmij(1, 2) - odejmij(5, 7))
