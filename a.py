numero_dia = int(input("Ingresa un número del 1 al 7 para representar un día de la semana: "))

nombre_dia = ""
switch = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

nombre_dia = switch.get(numero_dia, "Día no válido")

print("El nombre del día de la semana es:", nombre_dia)
