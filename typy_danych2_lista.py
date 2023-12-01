# lista - kolekcja, przechowuje dowolna ilosc danych dowolnego typu na raz
# zachowuje kolejnosc dodawania

lista = []  # pusta lista
print(lista)  # []
print(type(lista))  # <class 'list'>

# append() - dodawanie do listy
lista.append("Radek")
lista.append("Adek")
lista.append("Tadek")
lista.append("Rafał")
lista.append("Radek")
lista.append("Janek")
print(lista)  # ['Radek', 'Adek', 'Tadek', 'Rafał', 'Radek']
#                 0(-5)    1(-4)    2(-3)   3(-2)     4(-1)
print(lista[0])
print(lista[-0])
print(lista[-1])
print(len(lista))  # dlugosc listy
# print(lista[10])  # IndexError: list index out of range
print(lista[-3])
print(lista[5 - 7])
print(lista[0:3])  # ['Radek', 'Adek', 'Tadek']
print(lista[:3])  # ['Radek', 'Adek', 'Tadek']
print(lista[-2:0])  # []
print(lista[0:-2])  # []
print(lista[3:7])  # ['Rafał', 'Radek']
print(lista[0:-11])
print(lista[0:5:2])  # start stop krok
print(lista[0::2])  # ['Radek', 'Tadek', 'Radek']

# nadpisanie elementu na danym indeksie
lista[2] = "Mikołaj"
print(lista)

# dodanie elementy pomiedzy elementy we wskazanym miejscu
lista.insert(1, "Marcin")
print(lista)

# usunięcie elementu (pierwszy napotkany)
lista.remove("Radek")
print(lista)

# sprawdzanie indeksu elementu
indeks = lista.index("Marcin")
print(indeks)

# usuniecie elementu po numerze indeksu
print(lista.pop(indeks))  # Marcin - zwraca element usuniety
print(lista)
print(lista.pop())  # Janek - ostatni element

a = 1
b = 3
a = b
print(a)
b = 7
print(a)

lista2 = lista  # kopia referencji - adresu w pamieci
lista3 = lista.copy()  # kopia listy
lista.clear()  # usuniecie wszystkich elementów
print(lista2)  # []
print(lista)  # []
print(lista3)
print(id(lista2))  # 2406440751360
print(id(lista))  # 2406440751360
print(id(lista3))  # 2406443461376

liczby = [54, 999, 34, 22, 12.34, 687]
liczby2 = [54, 999, 34, 22, 12.34, 687, "ABC"]
print(liczby)
liczby.sort()
print(liczby)
print(liczby2)
# liczby2.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'

lista_osoby = ['radek', 'ola', 'zenek']
print(lista_osoby)
lista_osoby.sort(reverse=True)
print(lista_osoby)  # ['zenek', 'radek', 'ola']

lista_osoby.reverse()
print(lista_osoby)  # ['ola', 'radek', 'zenek']

# liczby[6] = 6666  # IndexError: list assignment index out of range
liczby[3] = 6666
print(liczby)

liczby.pop(3)
liczby.remove(34)

tekst = 'Python'
lista1 = [tekst]
print(lista1)  # ['Python']

# rozpakowanie sekwencji
lista2 = list(tekst)
print(lista2)  # ['P', 'y', 't', 'h', 'o', 'n']

tekst2 = "Radek Radek"
lista3 = list(tekst2)
print(lista3)  # ['R', 'a', 'd', 'e', 'k', ' ', 'R', 'a', 'd', 'e', 'k']
lista4 = list(lista1)
print(lista3)
krotka = tuple(lista4)
print(krotka)
print(type(krotka))  # <class 'tuple'>
