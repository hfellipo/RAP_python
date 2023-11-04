from tkinter import *

def abrir():
    print('Abrir')

def salvar():
    print('Salvar')

def ajuda():
    print('Ajuda')

def aritmetica(e):
    soma.set(soma.get() + parcela.get())

def exibe():
    l.config(text="v1=%d, v2=%s" % (v1.get(), v2.get()))

root = Tk()

principal = Menu(root)
arquivo = Menu(principal)
arquivo.add_command(label='Abrir', command=abrir)
arquivo.add_command(label='Salvar', command=salvar)
principal.add_cascade(label='Arquivo', menu=arquivo)
principal.add_command(label='Ajuda', command=ajuda)

soma = DoubleVar(root)
parcela = DoubleVar(root)
lsoma = Label(textvar=soma)
eparcela = Entry(textvar=parcela)
eparcela.bind('<Return>', aritmetica)

v1 = IntVar(root)
v2 = StringVar(root)
c1 = Checkbutton(text="V1", variable=v1, command=exibe)
c2 = Checkbutton(text="V2", variable=v2, command=exibe, onvalue="Sim", offvalue="Nao")
l = Label()

for widget in (lsoma, eparcela, c1, c2, l):
    widget.pack()

root.configure(menu=principal)
exibe()

root.mainloop()
