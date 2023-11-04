import tkinter as tk

# Função chamada ao clicar no botão
def mostrar_mensagem():
    label.config(text="Olá, Mundo!")

# Cria uma janela
janela = tk.Tk()
janela.title("Exemplo Tkinter")

# Cria um rótulo
label = tk.Label(janela, text="Pressione o botão para saudar")
label.pack()

# Cria um botão
botao = tk.Button(janela, text="Saudar", command=mostrar_mensagem)
botao.pack()

# Inicia a interface gráfica
janela.mainloop()
