# Funciones de la calculadora
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

# Display Menu
while True:
    print("""
seleccione opcion:
          
            1- Sumar 
            2- Restar
            3- Multiplicar
            4- dividir 
        """)

    valor = int(input("Elige una opcion: ") )     

    if valor == 1:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print(num1, "+", num2, "=", suma(num1, num2))
        break;
    if valor == 2:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print(num1, "-", num2, "=", resta(num1, num2))
        break;
    if valor == 3:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print(num1, "*", num2, "=", multiplicacion(num1, num2))
        break;
    if valor == 4:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print(num1, "/", num2, "=", division(num1, num2))
        break;
    else:
        print("Opcion invalida")
        break;
