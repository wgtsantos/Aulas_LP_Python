import tkinter as tk

janela = tk.Tk()
janela.title("Minha Interface gráfica com Python") # Titulo da Janela
janela.geometry("580x300") # Resolução da Janela

fonte_titulo = ("Verdana", 12, "bold") # Tipo da Fonte

# Criando o rotulo com Titulo dentro da janela
# Formatando o texto do Titulo
titulo = tk.Label(janela, 
                  text="Titulo da UI",
                  font=fonte_titulo,
                  fg="#000044")
# titulo.pack()  Inserindo o titulo na janela
titulo.grid(row=0, column=0, padx=140, pady=10)

fonte_texto = ("Arial", 10, "italic")
txt = "Lorem ipsum, dolor sit amet consectetur adipisicing elit. \n Veritatis illo voluptate, optio eos ipsa consequatur \n odit sit repudiandae amet delectus, tempore quibusdam iusto culpa deleniti, \n dolorum blanditiis? Sequi, dicta eligendi!"

texto = tk.Label(janela,
                 text=txt,
                 font=fonte_texto)
texto.grid(row=1, column=0, padx=70, pady=10)

janela.mainloop()