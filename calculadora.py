from tkinter import *

def presionar_boton(num):
    global texto_ecuacion

    texto_ecuacion = texto_ecuacion + str(num)
    
    etiqueta_ecuacion.set(texto_ecuacion)

def resultado():
    global texto_ecuacion
    
    try:
        total = str(eval(texto_ecuacion))

        etiqueta_ecuacion.set(total)

        texto_ecuacion = total

    except ZeroDivisionError:

        etiqueta_ecuacion.set("Error aritmetico")

        texto_ecuacion = ""

    except SyntaxError:

        etiqueta_ecuacion.set("SYNTAX ERROR")

        texto_ecuacion = ""

def clear():
    global texto_ecuacion

    etiqueta_ecuacion.set("")

    texto_ecuacion = ""


ventana = Tk()
ventana.title("Calculadora v1")
ventana.geometry("325x575")

texto_ecuacion = ""

etiqueta_ecuacion = StringVar()

etiqueta = Label(ventana, textvariable=etiqueta_ecuacion, font=("fixedsys",20), bg="white",width=24, height=2)
etiqueta.pack()

frame = Frame(ventana)
frame.pack()

boton1 = Button(frame, text=1, height=3, width=6, font=("fixedsys",10),
                 command=lambda: presionar_boton(1))
boton1.grid(row=2, column=0)

boton2 = Button(frame, text=2, height=3, width=6, font=("fixedsys",10),
                 command=lambda: presionar_boton(2))
boton2.grid(row=2, column=1)

boton3 = Button(frame, text=3, height=3, width=6, font=("fixedsys",10),
                 command=lambda: presionar_boton(3))
boton3.grid(row=2, column=2)

mas = Button(frame, text="+", height=3, width=6, font=("fixedsys",10),
                 command=lambda: presionar_boton("+"))
mas.grid(row=2, column=3)

boton4 = Button(frame, text=4, height=3, width=6, font=("fixedsys",10),
                 command=lambda: presionar_boton(4))
boton4.grid(row=1, column=0)

boton5 = Button(frame, text=5, height=3, width=6, font=("fixedsys",10),
                 command=lambda: presionar_boton(5))
boton5.grid(row=1, column=1)

boton6 = Button(frame, text=6, height=3, width=6, font=("fixedsys",10),
                 command=lambda: presionar_boton(6))
boton6.grid(row=1, column=2)

menos = Button(frame, text="-", height=3, width=6, font=("fixedsys",10),
                 command=lambda: presionar_boton("-"))
menos.grid(row=1, column=3)

boton7 = Button(frame, text=7, height=3, width=6, font=("fixedsys",10),
                 command=lambda: presionar_boton(7))
boton7.grid(row=0, column=0)

boton8 = Button(frame, text=8, height=3, width=6, font=("fixedsys",10),
                 command=lambda: presionar_boton(8))
boton8.grid(row=0, column=1)

boton9 = Button(frame, text=9, height=3, width=6, font=("fixedsys",10),
                 command=lambda: presionar_boton(9))
boton9.grid(row=0, column=2)

multiplicar = Button(frame, text="x", height=3, width=6, font=("fixedsys",10),
                 command=lambda: presionar_boton("*"))
multiplicar.grid(row=0, column=3)

CEe = Button(frame, text="C", height=3, width=6, font=("fixedsys",10),
                 command=clear)
CEe.grid(row=0, column=4)

boton0 = Button(frame, text=0, height=3, width=6, font=("fixedsys",10),
                 command=lambda: presionar_boton(0))
boton0.grid(row=3, column=1)

dividir = Button(frame, text="/", height=3, width=6, font=("fixedsys",10),
                 command=lambda: presionar_boton("/"))
dividir.grid(row=3, column=2)

decimal = Button(frame, text=",", height=3, width=6, font=("fixedsys",10),
                 command=lambda: presionar_boton(","))
decimal.grid(row=3, column=0)

Resultado = Button(frame, text="=", height=3, width=6, font=("fixedsys",10),
                 command=resultado)
Resultado.grid(row=3, column=4)

ventana.mainloop()
