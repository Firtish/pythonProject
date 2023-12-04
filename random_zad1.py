import random

# random - generator liczb pseudolosowych
print(random.randint(1, 6))  # int 1..6
print(random.randrange(1, 6))  # int 1..5
print(random.randrange(6))  # int 0..5
print(random.random())  # 0.7299632037926983 0..0.99999
print(random.random() * 10)  # 8.308534463911757 0..9.99999

lista = [5, 7, 45, 34.56]
print(random.choice(lista))

Wyniki = []
lista_lotto = list(range(1, 46))  # wygeneruje od 1.. 45
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)

print(random.choices(lista_lotto, k=6))  # [1, 18, 8, 27, 19, 27] losowanie z powtórzeniami
print(random.sample(lista_lotto, 6))  # [32, 8, 11, 42, 23, 38] losowanie bez powtórzeń
print(random.sample(lista_lotto, k=6))  # [32, 8, 11, 42, 23, 38] losowanie bez powtórzeń
