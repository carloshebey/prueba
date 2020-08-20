"""class students:
    pass #Palabra reservado para una clase vacia
students = students() #Objeto
type(students)"""

class Auto:

    Rojo = False
    #Color = Rojo
    def __init__(self,puertas = None, color = None):
        print("Se creo el objeto")
        self.puertas = puertas
        self.color = color

        if puertas is not None and color is not None:
            print(f"Se creo un auto de {puertas} puertas color {color}")
    def Fabricar(self):
        self.Rojo = True
    def confirmar_fabricacion(self):
        if (self.Rojo):
            print("Auto a sido coloreado")
        else:
            print("Aun no se a pintado")
autos=Auto("2","Rojo")
autos.confirmar_fabricacion()
autos.Fabricar()
autos.confirmar_fabricacion()