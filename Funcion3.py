num1_ = int(input("Numero 1 >> "))
num2_ = int(input("Numero 2 >> "))



def nulos(x = None, y = None):
    if num1_ == None or num2_ == None:
        print("No hay datos")
        return
    return x + y
suma = nulos(num1_,num2_)
print(f"La Suma es  {suma}")
