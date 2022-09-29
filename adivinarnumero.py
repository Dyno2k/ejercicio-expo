import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.geometry("350x150")
opcion = tk.IntVar()
varResta = tk.IntVar()
varSuma = tk.IntVar()
resultadoFinal = tk.IntVar()
window.resizable(False, False)

bandera = 0
def showMsj():
    global opcion,entryResta,entrySuma,varResta,varSuma,resultadoFinal
    if bandera == 0: 
        newFrame()
        msj.set("Pensa un numero de dos cifras que no sean iguales")
        nextButton = tk.Button(frame,text="Siguiente",command=next).pack(side="right")
   
    elif bandera == 1: 
        newFrame()
        msj.set("Ahora invierte las cifras del numero")
        backButton = tk.Button(frame,text="Atras",command=back).pack(side="left")
        nextButton = tk.Button(frame,text="Siguiente",command=next).pack(side="right")
    
    elif bandera == 2:
        newFrame()
        msj.set("El numero invertido es mayor que el numero pensado?")##
        si = tk.Radiobutton(frame,text="Si,es mayor",variable=opcion,value=1).pack()
        no = tk.Radiobutton(frame,text="No,es menor",variable=opcion,value=2).pack()
        backButton = tk.Button(frame,text="Atras",command=back).pack(side="left")
        nextButton = tk.Button(frame,text="Siguiente",command=next).pack(side="right")
        return opcion
    
    elif bandera == 3:
        newFrame()
        entryResta = tk.Entry(frame,width=5)
        backButton = tk.Button(frame,text="Atras",command=back).pack(side="left")
        if opcion.get() == 1:
            msj.set("Ahora resta el numero invertido menos el numero pensado")
            entryResta.pack()
            loadButton = tk.Button(frame,text="Cargar",command=validarResta).pack()
        if opcion.get() == 2:
            msj.set("Ahora resta el numero pensado menos el numero invertido")
            entryResta.pack()
            loadButton = tk.Button(frame,text="Cargar",command=validarResta).pack()
        return entryResta
    
    elif bandera == 4:
        newFrame()
        backButton = tk.Button(frame,text="Atras",command=back).pack(side="left")
        msj.set("ahora suma las dos cifras del numero pensado al principio")
        entrySuma = tk.Entry(frame,width=5)
        entrySuma.pack()
        loadButton = tk.Button(frame,text="Cargar",command=validarSuma).pack()
        return entrySuma
    
    elif bandera == 5:
        newFrame()
        calculoRestultadoFinal()
        msj.set(f"El numero que pensaste es: ")
        numeroFinal = tk.Label(frame,text=f"{resultadoFinal.get()}",font=("roboto",30),foreground="Red").pack()
        backButton = tk.Button(frame,text="Atras",command=back).pack(side="left")
        nextButton = tk.Button(frame,text="Jugar de nuevo",command=playAgain).pack(side="right")
    
def newFrame():
    global frame
    frame.pack_forget()
    frame = tk.LabelFrame(window)
    frame.pack(fill="both",expand="yes")
    labelMsj = tk.Label(frame,textvariable=msj,font=("roboto",10),justify="center").pack()
   
def playAgain():
    global bandera
    bandera = 0
    showMsj()
    return bandera

def validarResta():
    global varResta,entryResta
    valorResta = entryResta.get()
    if valorResta != "0" and valorResta!="" and valorResta.isnumeric():
        varResta.set(entryResta.get())
        next()
    elif valorResta == "0":
            messagebox.showwarning("Error","Debe ingresar un numero distinto a cero")
    else:
            messagebox.showwarning("Error","Debe ingresar un valor numerico")

  
def validarSuma():
    global varSuma,entrySuma
    valorSuma = entrySuma.get()
    if valorSuma != "0" and valorSuma!="" and valorSuma.isnumeric():
        varSuma.set(entrySuma.get())
        next()
    elif valorSuma == "0":
            messagebox.showwarning("Error","Debe ingresar un numero distinto a cero")
    else:
            messagebox.showwarning("Error","Debe ingresar un valor numerico")


def calculoRestultadoFinal():
    global opcion, resultadoFinal
    x = varResta.get() /9
    a=int(( varSuma.get() + x) / 2)
    b =int ((varSuma.get() - x) / 2)
    if opcion.get() == 1:
        valor = str(b)+str(a)
        resultadoFinal.set(int(valor))
        return resultadoFinal
    elif opcion.get() == 2:
        valor = str(a)+str(b)
        resultadoFinal.set(int(valor))
        return resultadoFinal

def next():
    global bandera
    bandera += 1
    showMsj()
    return bandera

def back():
    global bandera
    bandera -= 1
    showMsj()
    return bandera


msj = tk.StringVar()
frame = tk.LabelFrame(window)
frame.pack(fill="both",expand="yes")
textLabel = tk.Label(frame,textvariable=msj)
textLabel.pack()
showMsj()

window.mainloop()