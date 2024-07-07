# Funciones de la calculadora
# a la funcion suma le damos 2 argumentos que seran nuestros inputs mas adelante
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error Aritmetico"
    else:
        return num1 / num2
    
def exponentes(num1, num2):
    return pow(num1, num2)

# Funcion desechada de raiz cuadrada
# def sqrt(num1):
#     return num1 **1/2
    
# en caso de no encontrar una opcion valida dentro del diccionario, esta arroja un "error"
def sys_fail():
    return"Opcion invalida"

# Defino un diccionario que simula switches o botones, al "presionar" una opcion, esta ejecuta
# la operacion aritmetica deseada y correspondida por su key 
def switch(opcion, num1, num2):
    sw = {
        1: suma(num1, num2),
        2: resta(num1, num2),
        3: multiplicacion(num1, num2),
        4: division(num1, num2),
        5: exponentes(num1, num2),
    }
    return sw.get(opcion, sys_fail())

#funcion principal
def main():
    owo = 1
    while owo:
     print("""
________________Calculator__________________\n______________version 0.1.4_________________\n|
|   1.Sumar
|   2.Restar
|   3.Multiplicar
|   4.Dividir
|   5.Potencias
|
""")
     opcion = int(input("Seleccione una opcion: "))
     num1 = int(input("Ingresa el primer número: "))
     num2 = int(input("Ingresa el segundo número: "))
     print(switch(opcion, num1, num2))
     respuesta = input("desea realizar otra operacion?: \ny/n\n")
     try:
         if respuesta.lower() in ["y","yes"]:
            owo == 0
         else: 
             if respuesta.lower() in ["n", "no"]:
                 break;
     except TypeError:
        print("Ingresa un valor no numerico")
        break;

if __name__ == "__main__":
    main()
