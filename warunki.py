# instrukcja warunkowa
# uzależnia działanie programu od warunku
# instrukcje sterowania przepływem programu
# if
# if warunek:
#   komenda_do wykonania gdy warunek spełniony
# po : musi być conajmniej jedna komenda pythona

odp = True
if odp:
    print("Brawo")  # po : obowiązkowo wcięcie 4 spacje
else:
    print("Warunek False")
print("dalsza część programu")

if odp:
    pass  # nic nie robi

print("Dalej")

# podatek = 0.9  # 90%
# zarobki = float(input("Podaj dochód"))
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:  # od 10000..29999
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.6
#
# print(f"Zapłacisz {zarobki * podatek:.2f} pln")
# suma_zam = 150
# if suma_zam > 150:
#     rabacik = 25
# else:
#     rabacik = 0
#
# print(f"rabacik {rabacik}")
#
# rabat = 25 if suma_zam > 150 else 0
#
# print(f"rabat {rabat}")

# zasymulujamy system analizy logów
# dane przyjdą w zmeinnych
# na podstawie wartości zmeinnych będziemy mieli różne działanie
# console, email -> inny
# error -> critical, medium, -> inny
# w przypadku błędu w konsoli wypiszemy komunikat
error_mesage = "Stało się coś strasznego"
allert_system = "console"
error = "critical"

if allert_system == "console":
    print(error_mesage)
elif allert_system == 'email':
    if error == 'critical':
        print("Masz błąd krytyczny")
    elif error == 'medium':
        print("ostrzeżenie")
    else:
        print("Błąd inny, idź na kawę")
else:
    print("nie znam takiego systemu")

# napisać program test

import random

wynik = input("Dmuchnij w ekran napisz T kiedy skończysz")
dane = random.randint(1, 10)
dane2 = random.randint(1, 5)

if wynik == "T":
    print(f"Masz {dane} promila we krwi")
    if dane > 9:
        print("Achiwment powyżej 10 promila zdobyty")
        pytanie = input("By zdybyć dodatkowe punkty prosze o odpowiedz na pytanie. Jakiego koloru jest czerwony maluch")
        if pytanie == "czerwony":
            print(f"Glatulacje twoje promile teraz to {dane + dane2}")
        else:
            print("Jesteś głupi")
    elif dane > 5:
        print("Masz zabrane prawo jazdy")

else:
    print("Nie prawidłowo dmuchałeś w ekran")
