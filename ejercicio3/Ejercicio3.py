lista = []

añadir = input("Introduce lo que quieres añadir a la lista (espacio para salir): ")
while añadir != " ":
    lista.append(añadir)
    añadir = input("Introduce lo que quieres añador a la lista (espacio para salir): ")
palabra1 = input("introduce la nueva palabra de la lista: ")
palabra2 = input("Introduce una palabra de la lista la cual quieres reemplazar: ")
    
print("lista antes:", lista)
if palabra2 in lista:
    index = lista.index(palabra2)
    lista[index] = palabra1 
    print("lista despues:", lista)
else:
    print("Error, no se encontro la palabra en la lista.")
