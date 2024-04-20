
def menu():
    menuOpciones = "Bienvenido seleccione la operacion que quiera realizar:\n"\
        "1. Sumar \n"\
        "2. Restar \n"\
        "3. Multiplicar \n"\
        "4. Dividir \n"\
        "5. Salir \n"
    print(menuOpciones)

def ingresarNumero():
    numeroIngresado = input("Ingresa un número: ")
    try:
        numero = float(numeroIngresado)
        return numero
    except ValueError:
        print("Error: Debes ingresar un número no se permiten letras o caracteres especiales.")
        return ingresarNumero()

def ingresarNumeroDistintoDeCero():
    numeroIngresado = input("Ingresa un número: ")
    try:
        numero = float(numeroIngresado)
        if(numero == 0):
            print("No se puede dividir por 0 ingrese otro número")
            return ingresarNumero()
        else:
            return numero
    except ValueError:
        print("Error: Debes ingresar un número no se permiten letras o caracteres especiales.")
        return ingresarNumero()

#Funcion Sumar
def sumar():
    numero1 = ingresarNumero()
    numero2 = ingresarNumero()
    suma = numero1 + numero2
    print(f"{numero1} + {numero2} = {suma}")

#Funcion Restar
def restar():
    numero1 = ingresarNumero()
    numero2 = ingresarNumero()
    suma = numero1 - numero2
    print(f"{numero1} - {numero2} = {suma}")

#Funcion Multiplicar
def multiplicar():
    numero1 = ingresarNumero()
    numero2 = ingresarNumero()
    suma = numero1 * numero2
    print(f"{numero1} x {numero2} = {suma}")

#Funcion Dividir
def dividir():
    numero1 = ingresarNumero()
    numero2 = ingresarNumeroDistintoDeCero()
    division = numero1 / numero2
    print(f"{numero1} / {numero2} = {division}")

#Funcion Calculadora
def calculadora():
    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            sumar()
        elif opcion == "2":
            restar()
        elif opcion == "3":
            multiplicar()
        elif opcion == "4":
            dividir()
        elif opcion == "5":
            print("Saliendo de la calculadora...")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

calculadora()

"""
    COMENTARIO AGREGADO DESDE LAS RAMA_1
"""