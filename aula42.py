import tkinter as tk

def somar():
   try:
       num1 = float(input_1.get())
       num2 = float(input_2.get())
       result = num1 + num2
       msg_resultado.config(text=f"O soma dos números é igual a: {result}")
   except ValueError:
         msg_resultado.config(text=f"Entrada inválida de dados!")
         
janela = tk.Tk()

#Definir Tamanho da Janela e Centraliza-la na tela
l = 500
a = 400
l_tela = janela.winfo_screenwidth()
a_tela = janela.winfo_screenheight()
x = (l_tela - l) // 2
y = (a_tela - a) // 2
janela.geometry(f"{l}x{a}+{x}+{y}")

janela.title("Interface Python - Entrada de Informações do Usuário")

fonte_titulo = ("Verdana", 12, "bold") # Tipo da Fonte
titulo = tk.Label(janela, 
                  text="Somar Números",
                  font=fonte_titulo,
                  fg="#000044")
titulo.pack(pady=10) # Inserindo o titulo na janela
# titulo.grid(row=0, column=0, padx=10, pady=10)

label_1 = tk.Label(janela, text="Número 1: ", font=("Arial", 10, "bold"))
# label_1.grid(row=1, column=0, padx=1, pady=10)
label_1.pack()

input_1 = tk.Entry(janela, width=30)
# input_1.grid(row=1, column=1, padx=1, pady=10)
input_1.pack()

label_2 = tk.Label(janela, text="Número 2: ", font=("Arial", 10, "bold"))
# label_2.grid(row=1, column=0, padx=1, pady=10)
label_2.pack()

input_2 = tk.Entry(janela, width=30)
# input_2.grid(row=1, column=1, padx=1, pady=10)
input_2.pack()

botao = tk.Button(janela,
                  text="CALCULAR",
                  command=somar,
                  width=10,
                  height=2,
                  font=("Arial", 6, "bold"),
                  fg="#000000",
                  bg="#DCDCDC")

botao.pack(pady=15)

msg_resultado = tk.Label(janela,
                         text="",
                         font=("Arial", 10, "bold"),
                         fg="#000000")
msg_resultado.pack(pady=20)

janela.mainloop()