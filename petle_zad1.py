import random
from itertools import zip_longest

# pętle
# for - tzw iteracyjna

for i in range(10):  # 0..0
    print(i)

for i in range(1, 10):
    print(i)

my_string = "Radek"
for i in my_string:
    print(i)

lista_lotto = list(range(1, 46))  # wygeneruje od 1.. 45

for i in range(6):
    wyn = random.choice(lista_lotto)
    lista_lotto.remove(wyn)
    print(wyn)

for _ in range(4):
    print("Radek")
    print(_)

for i in range(10):
    if i % 2 == 0:
        print(i, "jest parzyste")

lista3 = [j for j in range(1, 10) if j % 2 == 0]
print(lista3)
for c in lista3:
    if c == 3:
        c += 1  # c = c +1
    print(c)

imiona = ['Radek', 'Asia', 'Zbyszek', 'Marcin']
for p in imiona:
    print(p)

# wyświetla elementy z listy wraz z indeksem

for p in imiona:
    print(f"{imiona.index(p)} {p}")

# enumerate() - numeruje kolekcje
for p in enumerate(imiona):
    print(p)

for p, o in enumerate(imiona):
    print(p, o)

for p, o in enumerate(imiona, start=1):
    print(p, o)
# 1 Radek
# 2 Asia
# 3 Zbyszek
# 4 Marcin

ludzie = ['Radek', 'Janek', 'Tomek', 'Marek', 'Adam']
wiek = [45, 56, 34, 45]
# Radek 45

# for x in range(len(ludzie)):
#     print(ludzie[x], wiek[x])

# zip() - łączenie kolekcji

for i in zip(ludzie, wiek):
    print(i)

for p, w in zip(ludzie, wiek):
    print(p, w)

zipped = zip_longest(ludzie, wiek, fillvalue=None)
print(type(zipped))  # <class 'itertools.zip_longest'>
zipped_list = list(zipped)
# nie wykona sie bo elementy zostały już odczytane
for name, age in zipped:
    print(name, age)

for name, age in zipped_list:
    print(name, age)
# Radek 45
# Janek 56
# Tomek 34
# Marek 45
# Adam None
# 0 Radek 45

for i in enumerate(zipped_list):
    print(i)

a, b = (4, ('Adam', 'None'))
print(a)
print(b)

c, d = b
print(a, c, d)

for i, (p, w) in enumerate(zipped_list):
    print(i, p, w)
# 0 Radek 45
# 1 Janek 56
# 2 Tomek 34
# 3 Marek 45
# 4 Adam None

for i in range(0, 10, 2):  # start, stop, krok
    print(i)

for i in range(10, 0, -2):
    print(i)

parzyste = [i for i in range(0, 10, 2)]
print(parzyste)  # [0, 2, 4, 6, 8]

c = {'name': 'Radek', 'age': '5'}
print({v: k for k, v in c.items()})  # {'Radek': 'name', '5': 'age'}
