import tkinter as tk

def clique():
    popup = tk.Toplevel()
    popup.title("Mensagem!")
    
    popup_msg = tk.Label(popup, text="Botão Clicado!")
    popup_msg.pack()
    
    botao_fechar = tk.Button(popup,
                           text="Fechar",
                           command=popup.destroy)
    botao_fechar.pack()
    

janela = tk.Tk()
janela.geometry("500x400")
janela.title("Interface Python com Botão de interação")

botao = tk.Button(janela,
                  text="Clique aqui",
                  command=clique,
                  width=12,
                  height=3,
                  font=("Arial", 12, "bold"),
                  fg="#0001F0",
                  bg="#DCDCDC")

botao.pack()

janela.mainloop()