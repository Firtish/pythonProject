import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
# y = [2,3,5,7,9]
y = [i ** 2 for i in x]
plt.plot(x, y)
plt.title("Wykr liniowy")
plt.xlabel("Oś X")
plt.ylabel("Oś Y")

plt.show()
