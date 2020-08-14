import math
radio = float(input("Radio >>:"))


def area_circulo(rad):
    return (math.pow(rad,2)) * math.pi

resultado = area_circulo(radio)
print(f"El area es {resultado:.4f}")