import math

class AlgebraVectorial:
    def __init__(self, a, b, c=0):
        self.a = a
        self.b = b
        self.c = c
    
    def __add__(self, other):
        return AlgebraVectorial(self.a + other.a, self.b + other.b, self.c + other.c)
    
    def __mul__(self, scalar):
        return AlgebraVectorial(self.a * scalar, self.b * scalar, self.c * scalar)
    
    def longitudVector(self):
        return math.sqrt(self.a**2 + self.b**2 + self.c**2)
    
    def normalVector(self):
        mag = self.longitudVector()
        return AlgebraVectorial(self.a / mag, self.b / mag, self.c / mag)
    
    def productoEscalar(self, other):
        return self.a * other.a + self.b * other.b + self.c * other.c
    
    def productoVectorial(self, other):
        return AlgebraVectorial(
            self.b * other.c - self.c * other.b,
            self.c * other.a - self.a * other.c,
            self.a * other.b - self.b * other.a
        )
    
    def es_perpendicular(self, other):
        return self.productoEscalar(other) == 0
    
    def es_paralelo(self, other):
        return self.productoVectorial(other).longitudVector() == 0
    
    def proyeccionVector(self, other):
        factor = self.productoEscalar(other) / (other.longitudVector() ** 2)
        return other * factor
    
    def componenteVector(self, other):
        return self.productoEscalar(other) / other.longitudVector()
    
    def __repr__(self):
        return f"({self.a}, {self.b}, {self.c})"

# Ejemplo de uso
v1 = AlgebraVectorial(3, 4, 5)
v2 = AlgebraVectorial(6, 8, 10)

print("Suma de v1 b v2:", v1 + v2)
print("Multiplicación de v1 por 2:", v1 * 2)
print("Magnitud de v1:", v1.longitudVector())
print("Vector normalizado de v1:", v1.normalVector())
print("Producto escalar de v1 b v2:", v1.productoEscalar(v2))
print("Producto vectorial de v1 b v2:", v1.productoVectorial(v2))
print("¿Son perpendiculares?", v1.es_perpendicular(v2))
print("¿Son paralelos?", v1.es_paralelo(v2))
print("Probección de v1 sobre v2:", v1.proyeccionVector(v2))
print("Componente de v1 en la dirección de v2:", v1.componenteVector(v2))



