# while - pętra sterowana warunkiem

licznik = 0
while True:
    licznik += 1
    print("komunikat!!")
    if licznik > 10:
        break  # przerwanie pętli

print(licznik)
licznik = 0
while licznik < 10:
    licznik += 1
    print("komunikat2!!!")

lista = []
lista2 = []
while True:
    wej = input("Podaj liczbę")
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista2.append(int(wej))

print(lista)
print(lista2)
# ['1', '2', '3', '4', '5', '6']
# [1, 2, 3, 4, 5, 6]
