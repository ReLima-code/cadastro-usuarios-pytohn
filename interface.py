import tkinter as tk
from tkinter import messagebox
import json
import os

ARQUIVO = "usuarios.json"

def carregar_usuarios():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_usuarios(lista):
    with open(ARQUIVO, "w") as f:
        json.dump(lista, f, indent=4)

def cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()

    if nome == "" or email == "":
        messagebox.showwarning("Erro", "Preencha todos os campos.")
        return

    usuarios.append({"nome": nome, "email": email})
    salvar_usuarios(usuarios)

    messagebox.showinfo("Sucesso", "Usuário cadastrado!")
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)

def listar():
    lista_box.delete(0, tk.END)
    for usuario in usuarios:
        lista_box.insert(tk.END, f"{usuario['nome']} - {usuario['email']}")

def buscar():
    termo = entry_busca.get().lower()
    lista_box.delete(0, tk.END)

    for usuario in usuarios:
        if termo in usuario["nome"].lower():
            lista_box.insert(tk.END, f"{usuario['nome']} - {usuario['email']}")

def remover():
    selecionado = lista_box.curselection()
    if not selecionado:
        messagebox.showwarning("Erro", "Selecione um usuário.")
        return

    indice = selecionado[0]
    usuarios.pop(indice)
    salvar_usuarios(usuarios)
    listar()

# Janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro de Usuários")
janela.geometry("400x400")

usuarios = carregar_usuarios()

# Campos
tk.Label(janela, text="Nome").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Label(janela, text="Email").pack()
entry_email = tk.Entry(janela)
entry_email.pack()

tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=5)
tk.Button(janela, text="Listar Usuários", command=listar).pack(pady=5)

tk.Label(janela, text="Buscar por nome").pack()

entry_busca = tk.Entry(janela)
entry_busca.pack()

tk.Button(janela, text="Buscar", command=buscar).pack(pady=5)
tk.Button(janela, text="Mostrar Todos", command=listar).pack(pady=5)

lista_box = tk.Listbox(janela)
lista_box.pack(fill=tk.BOTH, expand=True, pady=5)

tk.Button(janela, text="Remover Selecionado", command=remover).pack(pady=5)

janela.mainloop()
