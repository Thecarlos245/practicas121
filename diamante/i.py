class A:
    def __init__(self, x):
        self.x = x
    
    def metodo1(self):
        self.x = self.x + 1
        return self.x
        
class B:

    def __init__(self, y):
        self.y = y
    
    def metodo2(self):
        self.y = self.y + 1
        return self.y

class C(A, B):
    def __init__(self, x, y):
        A.__init__(self, x)
        B.__init__(self, y)
    
    def sumar(self):
        suma = self.x + self.y
        return f"x = {self.x}, y = {self.y}, Suma = {suma}"


print("Ingresa el valor para x:")
x = int(input())
print("Ingresa el valor para y:")
y = int(input())

objeto = C(x, y)


print("Valores iniciales:")
print(objeto.sumar())

print("\nmetodo1:")
objeto.metodo1()
print(objeto.sumar())

print("\nmetodo2:")
objeto.metodo2()
print(objeto.sumar())