# match case od pythona 3.10

lista = []
#lang = input("Podaj znany ci język programowania ")
lang = [1, 2, 3]
match lang:
    case "python":
        print("Lubie pythona")
        lista.append(lang)
    case "java":
        print("Java to kawa")
        lista.append(lang)
    case [a, b, c]:
        print(f"Lista z trzeba elementami {a} {b} {c}")
    case _:  # wartość domyślna
        print("Nie znam takiego")

print(lista)
