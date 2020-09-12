import tkinter as tk
from tkinter import ttk
from tkinter import *
import math

class StartPage:
	def __init__(self, root):
		self.root = root
		def update_a(*args):
			try:
				a_var.get() * 1.0
				text.set("La respuesta esta en tu corazon")
			except (ValueError, tk.TclError):
				text.set('Escriba bien los datos yoliberta :@')

		def update_b(*args):
			try:
				b_var.get() * 1.0
				text.set("La respuesta esta en tu corazon")
			except (ValueError, tk.TclError):
				text.set('Escriba bien los datos yoliberta :@')

		def update_c(*args):
			try:
				c_var.get() * 1.0
				text.set("La respuesta esta en tu corazon")
			except (ValueError, tk.TclError):
				text.set('Escriba bien los datos yoliberta :@')

		def update_t(*args):
			try:
				t_var.get() * 1.0
				text.set("La respuesta esta en tu corazon")
			except (ValueError, tk.TclError):
				text.set('Escriba bien los datos yoliberta :@')

		def formula(*args):
			try:
				aa = float(a.get())
				bb = float(b.get())
				cc = float(c.get())
				tt = float(t.get())
				solucion = cc + (1 - cc) / (1 - math.exp(-1.7 * aa * (tt - bb)))
				text.set("RTA:             {}".format(solucion))
			except:
				text.set("Error realizando la operacion, revisar datos.")

		text = tk.StringVar()
		text.set("La respuesta esta en tu corazon")
		sln = Label(root, textvariable=text)
		sln.place(x=290, y=290)

		a_label = Label(root, text="Digita la variable a:")
		a_label.place(x=50, y=100)
		a_var = tk.DoubleVar()
		a_var.trace('w', update_a) # call the update() function when the value changes
		a = ttk.Entry(root, textvariable= a_var)
		a.place(x=50, y=125)


		b_label = Label(root, text="Digita la variable b:")
		b_label.place(x=300, y=100)
		b_var = tk.DoubleVar()
		b_var.trace('w', update_b) # call the update() function when the value changes
		b = ttk.Entry(root, textvariable= b_var)
		b.place(x=300, y=125)


		c_label = Label(root, text="Digita la variable c:")
		c_label.place(x=50, y=150)
		c_var = tk.DoubleVar()
		c_var.trace('w', update_c) # call the update() function when the value changes
		c = ttk.Entry(root, textvariable= c_var)
		c.place(x=50, y=175)


		t_label = Label(root, text="Digita la variable Theta:")
		t_label.place(x=300, y=150)
		t_var = tk.DoubleVar()
		t_var.trace('w', update_t) # call the update() function when the value changes
		t = ttk.Entry(root, textvariable= t_var)
		t.place(x=300, y=175)

		cc= c.get()
		button = ttk.Button(root, text="Resolver", command = formula)
		button.place(x=50, y=290)

if __name__ == '__main__':
	root = Tk()
	root.title('Con amor para la mejor <3')
	canv = Canvas(root, width=500, height=400, bg='white')
	canv.grid(row=2, column=3)
	canv.pack()
	img = PhotoImage(file='tools/captura.png')
	canv.create_image(180, 10, anchor=NW, image=img)
	img_2 = PhotoImage(file='tools/aggt.png')
	canv.create_image(150, 220, anchor=NW, image=img_2)
	app = StartPage(root)
	root.mainloop()
