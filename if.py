## crear un programa que simule la entrada a un boliche. Debe dejar ingresar a la edad del usuario. Si es mayor a 18 mostrar por pantalla "puede ingresar", de lo contrario mostrar por pantalla "no puede ingresar.

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Puede ingresar.")
else:
    print("No puede ingresar.")
