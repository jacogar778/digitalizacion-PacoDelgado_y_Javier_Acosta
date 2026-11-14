lista = []
for i in range (5):
    numero = int(input("Introduce numeros enteros para añadir:"))
    lista.append(numero)
ordenada = sorted(lista)
if lista == ordenada:
    print("La lista esta ordenada de menor a mayor")
else:
    print("La lista no esta ordenada de menor a mayor")
