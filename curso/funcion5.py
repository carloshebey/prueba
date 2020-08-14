"""Realiza una funcion seperar lista() que tome una
 lista de numeros enteros
la primera con numeros pares y otra con los impares"""




list = []
list_par=[]
list_impar=[]

total_datos=int(input("Dame el total de datos a ingresar:"))
for n in range(0,total_datos):
    numero_nuevo=int(input("Ingrese los valores"))
    list.append(numero_nuevo)


def separar(listas):
    for avanzar in list:
        if avanzar %2==0 :
            list_par.append(avanzar)
        else:
            list_impar.append(avanzar)
    return list_par,list_impar        
list_par,list_impar = separar(list)
print(list_par)
print(list_impar)