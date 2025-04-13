class Persona:
    def __init__(self, Nombres, Apellidos, Edad):
        self.Nombres = Nombres
        self.Apellidos = Apellidos
        self.Edad = Edad

    def infoPersona(self):
        print(f'Los Nombres Son: {self.Nombres}')
        print(f'Los Apellidos Son: {self.Apellidos}')
        print(f'La Edad es de: {self.Edad} Años')

persona1 = Persona("Carlos Javier", "Castillo Lopez", 20)
persona1.infoPersona()