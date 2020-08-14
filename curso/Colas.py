cola = ["Jair", "Carlos","Emmanuel"]

cola.append("Monserrat")
import random
comienza = random.randint(0, 3)
n= cola.pop(comienza)
print(f"Atendiendo a {n}")
print(cola)