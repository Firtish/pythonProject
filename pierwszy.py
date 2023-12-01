print()  # wypisz/wydrukuj
print("Nazywam się Adrian")
print('Nazywam się Adrian')
# crtl d - powielenie linii z kursorem
# ctrl alt l - poprawia caly plik wedlug zasad pep8
print(type('Adrian'))
print(type("Adrian"))
# <class 'str'>
# <class 'str'>
# ctrl / - automatyczne komentowanie
print(39)
print(type(39))  # <class 'int'>

print("39" + "14")  # konkatenacja - łączenie stringów
print(5 * "4")
print(39 + 15)  # 54

imie: str = "Adrian"
print(imie)
print(type(imie))
imie: str = 39
print(imie)
print(type(imie))  # <class 'int'>
imie = "Adrian"
imie = "39"
wiek = 48
print(type(wiek))  # <class 'int'>
print(int(imie) + wiek)  # int() - rzutowanie na int
# print("14" + 50)  # TypeError: can only concatenate str (not "int") to str

wiek = "Adek"
print(type(wiek))
