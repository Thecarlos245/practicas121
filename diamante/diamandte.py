class A:
    def __init__(self,x,z):
        self.x = x
        self.z = z

    def incrementaXZ(self):
        self.x = self.x + 1
        self.z = self.z + 1
        return f"x = {self.x}, z = {self.z}"
        
    def incrementaZ(self):
        self.z = self.z + 1
        return f"z = {self.z}"
    
    
class B:
    def __init__(self,y,z):
        self.y = y
        self.z = z

    def incrementaYZ(self):
        self.y = self.y + 1
        self.z = self.z + 1
        return f"y = {self.y}, z = {self.z}"
        
    def incrementaZ(self):
        self.z = self.z + 1
        return f"z = {self.z}"
        

class C:
    def __init__(self,z):
        self.z = z
       
    def incrementaZ(self):
        self.z = self.z + 1
        return f"z = {self.z}"
        
       
class D(A,B,C):
    def __init__(self,x,y,z):
        A.__init__(self,x,z)
        B.__init__(self,y,z)
        C.__init__(self,z)
    
    def incrementaXYZ(self):
        self.z = self.z + 1
        self.x = self.x + 1
        self.y = self.y + 1
        return f"x = {self.x}, y = {self.y}, z = {self.z}"


d = D(5, 10, 3)
print("------En A incremento en ------")
print(d.incrementaXZ(),d.incrementaZ())
print("------En B incremento en ------")
print(d.incrementaYZ(),d.incrementaZ())
print("------En C incremento en ------")
print(d.incrementaZ())
print("------D------")
print(f"El final de cada incremento es x={d.x}, y={d.y}, z={d.z}")
   