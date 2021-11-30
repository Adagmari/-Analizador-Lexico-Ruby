from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from main import *
from sintactic import *

raiz = Tk()


raiz.geometry('800x400') # anchura x altura


raiz.configure(bg = 'white')

# Asigna un título a la ventana

raiz.title('Analizador Ruby')

Output = Text(raiz, height = 5, 
              width = 50, 
              bg = "light cyan")

Output.place(x=150, y=130)

def lexico():
    Output.delete('1.0', END) 
    mensaje = E1.get("1.0", "end-1c")
    texto1 = inputLex(mensaje)
    print(texto1) 
    Output.insert(END, texto1)
    print(mensaje) 

def sintactico():
    Output.delete('1.0', END)
    mensaje = E1.get("1.0", "end-1c")
    texto1 = inputSintactico(mensaje)
    print("texto1" , texto1) 
    Output.insert(END, texto1)
    print("mensaje", mensaje) 


def clearTextInput():
    
    E1.delete("1.0","end")    
    Output.delete("1.0","end")
    #label.config(text='')

L1 = Label(raiz, text = "Ingresar cadena")
L1.place(x=5, y=5)
L1 = Label(raiz, text = "Salida")
L1.place(x=5, y=130)
E1 = Text(raiz, height = 5, width = 50, bd=5)
E1.place(x=150, y=5)


ttk.Button(raiz, text='Léxico', command=lexico).place(x=150, y=250)
ttk.Button(raiz, text='Sintáctico', command=sintactico).place(x=250, y=250)
ttk.Button(raiz, text='Salir', command=quit).place(x=350, y=250)
ttk.Button(raiz, text='RESET', command=clearTextInput).place(x=450, y=250)

raiz.mainloop()