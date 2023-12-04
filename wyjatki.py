try:

    # print(5 / 0) # ZeroDivisionError: division by zero
    # print("a" / 2) # TypeError: unsupported operand type(s) for /: 'str' and 'int'
    # print(10 + "2")
    # print(int("A"))
    print(1 + 2)
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Błąd typu")
except ValueError:
    print("Błąd wartości")
except Exception as e:
    print("Błąd", e)
else:
    print("Tylko gdy nie ma błędu")
finally:
    print("Wykona się niezależnie czy błąd wystąpi czy nie")

print("Dalsza czesc programu")
# try - except [else,finally]

# program kalkulator
# ma wyswietlic menu - dodawanie, odejmowanie, mnożenie, dzielenie
# użyć pętli while
# może być if lub match case
# ma ładnie wydrukować wynik działania
# dodawanie 1 + 6 = 7
