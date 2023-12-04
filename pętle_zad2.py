dictionary = {'imie': 'Radek', 'nazwisko': 'kowalski'}
print(dictionary)
print(type(dictionary))

# wyświetli klucze
for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)

# wyświetlanie wartości
for k in dictionary.values():
    print(k)

for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => kowalski
