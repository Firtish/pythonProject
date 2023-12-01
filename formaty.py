user = "Tomek"  # str
wiek = 39  # int
wersja = 3.9000001  # <class 'float'>
print(type(wersja))
liczba = 123456789123
print(type(liczba))  # <class 'int'>

print("WItaj %s masz teraz %d lat" % (user, wiek))
# print("WItaj %d masz teraz %s lat" % (user, wiek))  # TypeError: %d format: a real number is required, not str
# %s - str
# %d - digit
print(("Witaj %(user)s, masz teraz %(wiek)d ") % {"user": user, "wiek": wiek})
# Witaj Tomek, masz teraz 39

print(f'Witaj {user}, masz teraz {wiek} lat.')  # f-string - string sformatowany
print("Uzywamy wersji pythona %i " % 3)
print("Uzywamy wersji pythona %f " % 3.12)  # fload Uzywamy wersji pythona 3.120000
print("Uzywamy wersji pythona %.2f " % 3.12)  # fload Uzywamy wersji pythona 3.12
print("Uzywamy wersji pythona %.f " % 3.12)  # fload Uzywamy wersji pythona 3
# wykonuje zaokraglenie
print(f"Używamy wersji python: {wersja}")
print(f"Używamy wersji python: {wersja:20f}")  # Używamy wersji python:             3.900000

print(f"{user:>20}")  # "               Tomek"
print(f"{user:<20}")  # "Tomek               "
print(f"{user:^20}")  # "       Tomek        "

print(liczba)  # 123456789123
print("Nasza duza liczba {:,}".format(liczba))
print("Nasza duza liczba {:,}".format(liczba).replace(","," "))
print("Nasza duza liczba {:,}".format(liczba).replace(",","."))
print(f"liczba {liczba:,}".replace(","," "))
