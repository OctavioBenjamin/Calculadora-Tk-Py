from tkinter import *

ventana = Tk()
ventana.config(background = '#212121')
ventana.title('Calculadora')


def selec():
    ventana.config(text="{}".format(opcion.get()))

opcion = IntVar()


EtqNum1 = Label(ventana, text = "Numero Uno", bg = '#212121', fg = 'white')
EtqNum2 = Label(ventana, text = "Numero Dos", bg = '#212121', fg = 'white')

EtqNum1.grid(row = 0, sticky="W")
EtqNum2.grid(row = 1, sticky="W")

CajaNum1 = Entry(ventana)
CajaNum2 = Entry(ventana)

CajaNum1.grid(row = 0, column = 1, sticky="W")
CajaNum2.grid(row = 1, column = 1, sticky="W")


def Num1():
    return int(CajaNum1.get())
def Num2():
    return int(CajaNum2.get())

def Igualar():
    if(opcion.get() == 1):
        return Num1()+Num2()
    elif(opcion.get() == 2):
        return Num1()-Num2()
    elif(opcion.get() == 3):
        return Num1()*Num2()
    elif(opcion.get() == 4):
        return Num1()/Num2()


opcion = IntVar()
suma = Radiobutton(ventana, text="Suma", variable=opcion, value=1, command=selec, 
                    bg = '#212121', fg = 'white')
resta = Radiobutton(ventana, text="Resta", variable=opcion, value=2, command=selec, 
                    bg = '#212121', fg = 'white')
mult = Radiobutton(ventana, text="Multiplicacion", variable=opcion, value=3, command=selec, 
                    bg = '#212121', fg = 'white')
div = Radiobutton(ventana, text="Division", variable=opcion, value=4, command=selec, 
                    bg = '#212121', fg = 'white')


suma.grid(column = 0, sticky="W")
resta.grid(column = 0, sticky="W")
mult.grid(column = 0, sticky="W")
div.grid(column = 0, sticky="W")


final = Label(ventana, text = "Resultado", width = 10, bg = 'white')
final.grid(column = 0, row = 8)

def resultado():
    final["text"] = Igualar()

Igual = Button(ventana, text = "Igualar", command = resultado, cursor = "hand2", bg = '#101010', 
                fg = 'white', relief="raised", highlightthickness=0)
Igual.grid(column = 0, row = 6)


ventana.mainloop()