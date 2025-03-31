import math

class AlgebraVectorial:
    def __init__(self, a, b, c=0):
        self.a = a
        self.b = b
        self.c = c
    
    def __add__(self, other):
        return AlgebraVectorial(self.a + other.a, self.b + other.b, self.c + other.c)
    
    def __sub__(self, other):
        return AlgebraVectorial(self.a - other.a, self.b - other.b, self.c - other.c)
    
    def __mul__(self, scalar):
        return AlgebraVectorial(self.a * scalar, self.b * scalar, self.c * scalar)
    
    def productoEscalar(self, other):
        return self.a * other.a + self.b * other.b + self.c * other.c
    
    def productoVectorial(self, other):
        return AlgebraVectorial(
            self.b * other.c - self.c * other.b,
            self.c * other.a - self.a * other.c,
            self.a * other.b - self.b * other.a
        )
    
    def magnitudVectorial(self):
        return math.sqrt(self.a**2 + self.b**2 + self.c**2)
    
    def es_perpendicular(self, other):
        return self.productoEscalar(other) == 0
    
    def es_paralelo(self, other):
        return self.productoVectorial(other).magnitudVectorial() == 0
    
    def proyeccion(self, other):
        factor = self.productoEscalar(other) / (other.magnitudVectorial() ** 2)
        return other * factor
    
    def componente(self, other):
        return self.productoEscalar(other) / other.magnitudVectorial()
    
    def __str__(self):
        return f"({self.a}, {self.b}, {self.c})"

# Ejemplo de uso
v1 = AlgebraVectorial(3, 4, 0)
v2 = AlgebraVectorial(6, 8, 0)

print("¿Son perpendiculares?", v1.es_perpendicular(v2))
print("¿Son paralelos?", v1.es_paralelo(v2))
print("Proyección de v1 sobre v2:", v1.proyeccion(v2))
print("Componente de v1 en la dirección de v2:", v1.componente(v2))





