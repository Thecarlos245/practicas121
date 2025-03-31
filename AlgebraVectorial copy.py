import math

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def sumar(self, a):
        return Vector(self.x + a.x, self.y + a.y, self.z + a.z)
    
    def restar(self, b):
        return Vector(self.x - b.x, self.y - b.y, self.z - b.z)
    
    def producto_vectorial(self, c):
        return Vector(
            self.y * c.z - self.z * c.y,
            self.z * c.x - self.x * c.z,
            self.x * c.y - self.y * c.x
        )
    
    def magnitud(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def mostrar(self):
        return f"<{self.x}, {self.y}, {self.z}>"

class AlgebraVectorial:
    @staticmethod
    def es_perpendicular(a, b):
        return a.sumar(b).magnitud() == a.restar(b).magnitud()
    
    @staticmethod
    def es_perpendicular_producto_punto(a, b):
        return a.x * b.x + a.y * b.y + a.z * b.z == 0
    
    @staticmethod
    def es_perpendicular_criterio(a, b):
        suma_cuadrados = a.magnitud() ** 2 + b.magnitud() ** 2
        magnitud_suma_cuadrada = a.sumar(b).magnitud() ** 2
        return magnitud_suma_cuadrada == suma_cuadrados
    
    @staticmethod
    def es_paralelo(a, b):
        return a.producto_vectorial(b).magnitud() == 0
    
    @staticmethod
    def es_paralelo_factor(a, b, r):
        return (a.x / b.x == r) and (a.y / b.y == r) and (a.z / b.z == r)
    
    @staticmethod
    def proyeccion(a, b):
        producto_punto = a.x * b.x + a.y * b.y + a.z * b.z
        magnitud_cuadrada = b.magnitud() ** 2
        factor = producto_punto / magnitud_cuadrada
        return Vector(b.x * factor, b.y * factor, b.z * factor)
    
    @staticmethod
    def componente(a, b):
        producto_punto = a.x * b.x + a.y * b.y + a.z * b.z
        return producto_punto / b.magnitud()

if __name__ == "__main__":
    a = Vector(2, 4, 6)
    b = Vector(0, 0, 0)
    c = Vector(10, -3, -1)
    d = AlgebraVectorial.proyeccion(a, c)
    
    print(f"¿Los vectores {a.mostrar()} y {b.mostrar()} son perpendiculares?: {AlgebraVectorial.es_perpendicular(a, b)}")
    print(f"¿Los vectores {a.mostrar()} y {c.mostrar()} son perpendiculares?: {AlgebraVectorial.es_perpendicular_producto_punto(a, c)}")
    print(f"¿Los vectores {c.mostrar()} y {a.mostrar()} son paralelos?: {AlgebraVectorial.es_paralelo(c, a)}")
    print(f"La proyección de a sobre c = {d.mostrar()}")
    print(f"El componente de a en c = {AlgebraVectorial.componente(a, c)}")


