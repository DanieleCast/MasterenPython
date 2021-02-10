'''
Crear una lista que contenga 8 número y permita:
-Recorrer y mostar todos los elementos
-Ordenar y mostarla
-Buscar algún elemento que el usuario pida por teclado
'''
def recorrer(lista):
    resultado=""
    for numbers in lista:
        resultado += str(numbers) + " "
    return resultado

elemento=None
numeros= [1, 4, 8, 12, 14, 88, 2, 11]
numeros.sort()
cadena = recorrer(numeros)
print("-------------------------------------------")
print(cadena)
while not isinstance(elemento,int):
    try:
        elemento=int(input("Ingrese el numero que quiere buscar: "))
        break
    except ValueError:
        print("Debes ingresar un numero Entero")    

if elemento in numeros:
    print(f"el numero {elemento} SI se encuentra en la lista")
else :
    print(f"el numero {elemento} NO se encuentra en la lista")


print(f"Tu lista tiene una longitud de {len(numeros)} elementos")