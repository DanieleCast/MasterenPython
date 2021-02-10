''' Añadir valos a lista mientras longitud < 120'''
'''
lista=[]
while len(lista) < 5:
    valor=input("Ingrese un valor en la lista: ")
    lista.append(valor)
print("\n")
print(f"La lista es: {lista}")

lista1=[]
for element in range(5):
    value=input("Insert a Value in the list: ")
    lista1.append(value)
print("\n")
print(f"Your second list is: {lista1}")
'''
'''Verificar si una cadena esta vacía y si lo está rellenarla con contenido en minuscula y mostrar en
mayusculas'''
def refill(string):
    if len(string.strip())==0:
        string="Esta cadena ya no está vacía"
        print(f"{string.upper()}")
    else: 
        print(f"Su cadena tiene contenido y es : {string}")
    return string

cadena="  "
new_string=refill(cadena)

