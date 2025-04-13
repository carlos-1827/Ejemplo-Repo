##Ejemplo Clase
class OpNumeros:
    def __init__(self,Num1,Num2,Num3):
        self.Num1 = Num1
        self.Num2 = Num2
        self.Num3 = Num3

    def Sumar(self):
        return self.Num1 + self.Num2 + self.Num3
        
    def Restar(self):
        return self.Num1 - self.Num2 - self.Num3
        
    def Multiplicar(self):
        return self.Num1 * self.Num2 * self.Num3

    def Dividir(self):
        return self.Num1 / self.Num2 / self.Num3

obj = OpNumeros(50,30,20)
print('La suma de los Numeros es:', obj.Sumar())
print('La Resta de los Numeros es:', obj.Restar())
print('La Multiplicacion de los Numeros es:', obj.Multiplicar())
print(f'La División es:', obj.Dividir())