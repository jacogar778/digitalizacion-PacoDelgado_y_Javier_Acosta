"""
Pide al usuario una clave y muestra su valor. Si la clave existe, muestra "Esa calve no existe".
"""

pokemon = {"Nombre": "Pikachu", "Tipo":"Eléctrico", "Nivel": "25"}
clave = input ("Dime una clave: ")

print(pokemon.get(clave, "Esa clave no existe."))