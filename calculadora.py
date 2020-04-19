from tkinter import *
from tkinter import messagebox

raiz=Tk()

raiz.title("Awsome Calc")
raiz.iconbitmap("calc.ico")

marco=Frame(raiz,bg="black")

marco.pack()
BarraMenu=Menu(raiz)

raiz.config(menu=BarraMenu, width=300, height=300)




#---------------------pantalla----------------------------------------#
numeroPantalla=StringVar()
pantallaHistoria=StringVar()
numeroHistorico=DoubleVar()
tipo_op=StringVar()
n_operando=BooleanVar()

def construir_iterac(tipo_operacion, operador_en_string):

	if numeroHistorico.get()==0:
		pantallaHistoria.set(pantallaHistoria.get() + numeroPantalla.get()+ operador_en_string)
		numeroHistorico.set(numeroPantalla.get())
		numeroPantalla.set("0")
		tipo_op.set(tipo_operacion)

	else:
		pantallaHistoria.set(pantallaHistoria.get() + numeroPantalla.get()+ operador_en_string)
	
		if tipo_op.get()=="suma":

			resultado=numeroHistorico.get()+float(numeroPantalla.get())

		elif tipo_op.get()=="resta":
			
			resultado=numeroHistorico.get()-float(numeroPantalla.get())
		
		elif tipo_op.get()=="multi":
			
			resultado=numeroHistorico.get()*float(numeroPantalla.get())

		elif tipo_op.get()=="dividir":
			
			resultado=numeroHistorico.get()/float(numeroPantalla.get())

		elif tipo_op.get()=="porcien":
			
			resultado=numeroHistorico.get()*(int(numeroPantalla.get()))/100

		numeroHistorico.set(resultado)
		
		if "." in str(resultado) and str(resultado).endswith("0"):
			resultado_s=str(resultado)
			numeroPantalla.set(resultado_s[0:len(resultado_s)-2])
		else:
			numeroPantalla.set(str(resultado))

		n_operando.set(False)
		tipo_op.set(tipo_operacion)

def crear_boton(fila, columna,texto_boton, funcion):
		texto_boton=Button(marco, text=texto_boton, width=10 , height=3 ,font=("NI7seg",10), bg="#353B3C",fg="#03f943", cursor="hand2",  command=funcion)
		texto_boton.grid(row=fila, column=columna)
	
pantallaH=Entry(marco, textvariable=pantallaHistoria, bd=0,width=15)
pantallaH.grid(row=0, column= 1,padx=10, pady=2, columnspan=4, sticky="nsew")
pantallaH.config(bg="black", fg="#03f943", font=("NI7seg",15), justify=RIGHT)

pantalla=Entry(marco, textvariable=numeroPantalla, bd=0, width=15)
pantalla.grid(row=1, column= 1, padx=10, pady=2,columnspan=4)
pantalla.config(bg="black", fg="#03f943", font=("NI7seg",25), justify=RIGHT)

#..............................pulsa teclado.............................


def igual():
	
	if tipo_op.get()=="suma":
		resultado=numeroHistorico.get()+float(numeroPantalla.get())
		pantallaHistoria.set(pantallaHistoria.get() + numeroPantalla.get()+ "=")

	elif tipo_op.get()=="resta":
		resultado=numeroHistorico.get()-float(numeroPantalla.get())
		pantallaHistoria.set(pantallaHistoria.get() + numeroPantalla.get()+ "=")

	elif tipo_op.get()=="multi":
		resultado=numeroHistorico.get()*float(numeroPantalla.get())
		pantallaHistoria.set(pantallaHistoria.get() + numeroPantalla.get()+ "=")

	elif tipo_op.get()=="dividir":
		resultado=numeroHistorico.get()/float(numeroPantalla.get())
		pantallaHistoria.set(pantallaHistoria.get() + numeroPantalla.get()+ "=")

	elif tipo_op.get()=="porcien":
		resultado=numeroHistorico.get()*(float(numeroPantalla.get()))/100
		pantallaHistoria.set(pantallaHistoria.get() + numeroPantalla.get()+ "% =")


	if "." in str(resultado) and str(resultado).endswith("0"):
		resultado_s=str(resultado)
		numeroPantalla.set(resultado_s[0:len(resultado_s)-2])
	else:
		numeroPantalla.set(str(resultado))

	numeroHistorico.set(0)
	n_operando.set(False)


def NumeroPulsado(num):

	if "." in numeroPantalla.get() and num == ".":

		numeroPantalla.set(numeroPantalla.get())

	else:

		if n_operando.get()==False:
			numeroPantalla.set(num)
			n_operando.set(True)

		else:
			if numeroPantalla.get()!="0":

				numeroPantalla.set(numeroPantalla.get()+ num)

			else:
				if num==".":
					numeroPantalla.set(numeroPantalla.get()+ num)
				else:
					numeroPantalla.set(num)

def Borrar_ultimo():
	cadena_Pantalla=numeroPantalla.get()
	numeroC=cadena_Pantalla[0:len(cadena_Pantalla)-1]
	
	if numeroC== "":

		numeroPantalla.set("0")

	else:

		numeroPantalla.set(numeroC)

def borrar_todo():
	pantallaHistoria.set("")
	numeroPantalla.set("0")
	numeroHistorico.set(0)
	n_operando.set(True)

def borrar_pantalla():
	numeroPantalla.set("0")

def Pegar():
	obtenido=raiz.clipboard_get()
	numeroPantalla.set(obtenido)

def Cortar():
	raiz.clipboard_clear()
	obtenido=raiz.clipboard_append(numeroPantalla.get())
	numeroPantalla.set("0")

def Copiar():
	raiz.clipboard_clear()
	obtenido=raiz.clipboard_append(numeroPantalla.get())

def salirAplicacion():
	respuesta=messagebox.askquestion("Salir", "¿Deseas salir de la calculadora ?")
	if respuesta=="yes":
		raiz.destroy()

def infoAdicional():
	messagebox.showinfo("Calculadora Simple", "Calculadora simple de numeros enteros y decimales 2020")

def avisoLic():
	messagebox.showwarning("Licencia", "Calculadora realizada por el ingeniero Samuel Gomez bajo GNU")

#__________________________ Grafica__________________________________

Archivo_Menu=Menu(BarraMenu, tearoff=0)
Archivo_Menu.add_command(label="Salir", command= salirAplicacion)

Edicion_Menu=Menu(BarraMenu, tearoff=0)
Edicion_Menu.add_command(label="Copiar", command=Copiar)
Edicion_Menu.add_command(label="Cortar", command=Cortar)
Edicion_Menu.add_command(label="Pegar", command=Pegar)

Ayuda_Menu=Menu(BarraMenu, tearoff=0)
Ayuda_Menu.add_command(label="Licencia", command=avisoLic)
Ayuda_Menu.add_command(label="Acerca de...", command=infoAdicional)
Ayuda_Menu.add_separator()


Ayuda_sub_menu=Menu(Ayuda_Menu, tearoff=0)
Ayuda_sub_menu.add_command(label="Ir a pagina web 1")
Ayuda_sub_menu.add_command(label="Ir a pagina web 2")

BarraMenu.add_cascade(label="Archivo" , menu=Archivo_Menu)
BarraMenu.add_cascade(label="Edicion" , menu=Edicion_Menu)
BarraMenu.add_cascade(label= "Ayuda", menu=Ayuda_Menu)
Ayuda_Menu.add_cascade(label="ir a la documentacion", menu=Ayuda_sub_menu)


#----------------------------fila 1---------------------------------------

crear_boton(2, 1, "%", lambda:construir_iterac("porcien","<="))

crear_boton(2, 2, "C", borrar_todo)

crear_boton(2, 3, "CE", borrar_pantalla)

crear_boton(2, 4, "<=",Borrar_ultimo)

#----------------------------fila 2---------------------------------------

crear_boton(3, 1, "7", lambda:NumeroPulsado("7"))

crear_boton(3, 2, "8", lambda:NumeroPulsado("8"))

crear_boton(3, 3, "9", lambda:NumeroPulsado("9"))

crear_boton(3, 4, "/", lambda:construir_iterac("dividir","/"))

#----------------------------fila 3---------------------------------------

crear_boton(4, 1, "4", lambda:NumeroPulsado("4"))

crear_boton(4, 2, "5", lambda:NumeroPulsado("5"))

crear_boton(4, 3, "6", lambda:NumeroPulsado("6"))

crear_boton(4, 4, "x", lambda:construir_iterac("multi","x"))

#----------------------------fila 4---------------------------------------

crear_boton(5, 1, "1", lambda:NumeroPulsado("1"))

crear_boton(5, 2, "2", lambda:NumeroPulsado("2"))

crear_boton(5, 3, "3", lambda:NumeroPulsado("3"))

crear_boton(5, 4, "-", lambda:construir_iterac("resta","-"))

#----------------------------fila 5---------------------------------------

crear_boton(6, 1, "0", lambda:NumeroPulsado("0"))

crear_boton(6, 2, ".", lambda:NumeroPulsado("."))

crear_boton(6, 3, "=", igual)

crear_boton(6, 4, "+", lambda:construir_iterac("suma","+"))

raiz.mainloop()