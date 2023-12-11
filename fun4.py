# funkcja zagnieżdżona
def fun1():
    print("To jest fun1")

    def fun2():  # definicja funkcji - zapamiętanie adresu
        print("To jest fun2")

    return fun2


print(fun1())  # <function fun1.<locals>.fun2 at 0x00000232FFBC9440>
xFun = fun1()
print(xFun)
print(type(xFun))
xFun()  # To jest fun2
