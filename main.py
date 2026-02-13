import tkinter as tk
from tkinter import messagebox

usuarios = []

def cadastrar_usuario():
    nome = entry_nome.get()
    email = entry_email.get()

    if nome == "" or email == "":
        messagebox.showwarning("Erro", "Preencha todos os campos!")
        return

    usuarios.append(f"{nome} - {email}")
    atualizar_lista()

    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)

def atualizar_lista():
    listbox.delete(0, tk.END)
    for usuario in usuarios:
        listbox.insert(tk.END, usuario)

# Janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro de Usuários")
janela.geometry("400x300")

# Labels e entradas
tk.Label(janela, text="Nome").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Label(janela, text="Email").pack()
entry_email = tk.Entry(janela)
entry_email.pack()

# Botão
tk.Button(janela, text="Cadastrar", command=cadastrar_usuario).pack(pady=10)

# Lista
listbox = tk.Listbox(janela, width=50)
listbox.pack()

janela.mainloop()
