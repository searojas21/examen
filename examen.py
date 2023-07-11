from datetime import datetime
from random import randint
from random import choice
comprada=""
nombreapellido=""
rut=0
piso = [""] * 40  
precios = {"TipoA": 3800, "TipoB": 3000, "TipoC": 2800, "TipoD": 3500}  
compradores = []  
tipo_departamento = {"TipoA": 0, "TipoB": 0, "TipoC": 0, "TipoD": 0}  
def comprar_departamento():

    departamento= int(input("Elija el departamento del piso(1 a 4): "))
    if departamento < 1 or departamento > 4:
        print("Solo existen 4 departamentos por piso es decir elejir entre 1 y 4")
        return

    comprada = []  

    for i in range(departamento):
        mostrar_departamentos_disponibles()
        disponibles= int(input("Seleccione el departamento disponible: "))

        if piso[disponibles - 1] != "":
            print("No está disponible")
            i -= 1
            return

        comprada.append(disponibles)

    rut= int(input("Ingrese el rut sin puntos ni guión y sin dígito verificador: "))
    if rut < 0 or rut > 99999999:
        rut = input("Rut inválido,Porfavor ingresar solo los primeros 8 dígitos de su rut: ")

    nombreApellido = input("Ingresarsu nombre y apellido: ")
    while nombreApellido == "":
        nombreApellido = input("Por favor ingrese un nombre y apellido: ")

compradores.append({
        "rut":rut,
        "nombreApellido":nombreapellido
    })

for disponibles in comprada:
        if disponibles <= 10:
            piso[disponibles - 1] = "TipoA"
            tipo_departamento["TipoA"] += precios["TipoA"]
        elif disponibles >= 11 and disponibles <= 30:
            piso[disponibles - 1] = "TipoB"
            tipo_departamento["TipoB"] += precios["TipoB"]
        elif disponibles >= 31 and disponibles <= 40:
            piso[disponibles - 1] = "TipoC"
            tipo_departamento["TipoC"] += precios["TipoC"]
        else:
            piso[disponibles - 1] = "TipoD"
            tipo_departamento["TipoD"] += precios["TipoD"]

def mostrar_departamentos_disponibles():
    
    for i in range(40):
        if i % 10 == 0:
            print()
        if piso[i] == "":
            print(i + 1, end=" ")
        else:
            print("X", end=" ")
    print()


def ver_listado_compradores():
   
    compradores.sort()  
    for i, rut in enumerate(compradores):
        print(i + 1, rut)

def mostrar_ganancias_totales():
   
    total = 0 

    for tipo, monto in tipo_departamento.items():
        total += monto 
        print(f"{tipo}: {monto}")

    print(f"Total: {total}")


def salir():
    
    for nombreApellido in compradores:
        print("Gracias por su tiempo, ", nombreApellido["nombreApellido"], datetime.now())

def menu_principal():

    opcion = 0

    while opcion != 5:
        print("*****Casa Feliz*****")
        print("1. Comprar departamento")
        print("2. Mostrar departamentos disponibles")
        print("3. Ver listado de compradores")
        print("4. Mostrar ganancias totales")
        print("5. Salir")

        opcion = input("Ingrese la opción que desea: ")

        if opcion == "1":
            comprar_departamento()
        elif opcion == "2":
            mostrar_departamentos_disponibles()
        elif opcion == "3":
            ver_listado_compradores()
        elif opcion == "4":
            mostrar_ganancias_totales()
        elif opcion == "5":
            salir()
            break
        else:
            print("Opción inválida")

menu_principal()
