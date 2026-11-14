contador1 = 0
contador2 = 0
lista1 = []
lista2 = []
palabra_lista1 = input("Cuantas palabras quieres introducir en la lista1")
palabra_lista1 = input("Cuantas palabras quieres introducir en la lista2")
for i in range(palabra_lista1):
    palabra = input("Introduce una palabra")
    lista1.append(palabra)
for i in range(palabra_lista2):
    palabra = input("Introduce una palabra")
    lista2.append(palabra)
print("lista1:",lista1)
print("lista2:",lista2)
for i in lista2:
    if i in lista1:
        lista1.remove(i)
print("la nueva lista 1 es:",lista1)
