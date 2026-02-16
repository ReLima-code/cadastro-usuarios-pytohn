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

def editar():
    selecionado = lista_box.curselection()

    if not selecionado:
        messagebox.showwarning("Erro", "Selecione um usuário para editar.")
        return

    indice = selecionado[0]

    novo_nome = entry_nome.get()
    novo_email = entry_email.get()

    if novo_nome == "" or novo_email == "":
        messagebox.showwarning("Erro", "Preencha nome e email.")
        return

    usuarios[indice] = {"nome": novo_nome, "email": novo_email}
    salvar_usuarios(usuarios)
    listar()

    messagebox.showinfo("Sucesso", "Usuário atualizado!")


# Janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro de Usuários")
janela.geometry("700x300")
janela.resizable(False, False)

usuarios = carregar_usuarios()

# ================= FRAME FORMULÁRIO =================
frame_form = tk.Frame(janela, padx=15, pady=10)
frame_form.pack(fill="x")

tk.Label(frame_form, text="Nome").grid(row=0, column=0, sticky="w")
entry_nome = tk.Entry(frame_form, width=30)
entry_nome.grid(row=0, column=1, padx=10)

tk.Label(frame_form, text="Email").grid(row=1, column=0, sticky="w")
entry_email = tk.Entry(frame_form, width=30)
entry_email.grid(row=1, column=1, padx=10)

tk.Button(frame_form, text="Cadastrar", width=15, command=cadastrar)\
    .grid(row=0, column=2, padx=10)

tk.Button(frame_form, text="Editar", width=15, command=editar)\
    .grid(row=1, column=2, padx=10)

# ================= FRAME BUSCA =================
frame_busca = tk.Frame(janela, padx=15, pady=10)
frame_busca.pack(fill="x")

tk.Label(frame_busca, text="Buscar por nome").grid(row=0, column=0, sticky="w")
entry_busca = tk.Entry(frame_busca, width=30)
entry_busca.grid(row=0, column=1, padx=10)

tk.Button(frame_busca, text="Buscar", width=12, command=buscar)\
    .grid(row=0, column=2, padx=5)

tk.Button(frame_busca, text="Mostrar Todos", width=12, command=listar)\
    .grid(row=0, column=3, padx=5)

# ================= FRAME LISTA =================
frame_lista = tk.Frame(janela, padx=15, pady=10)
frame_lista.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side="right", fill="y")

lista_box = tk.Listbox(
    frame_lista,
    yscrollcommand=scrollbar.set,
    width=70,
    height=12
)
lista_box.pack(fill="both", expand=True)

scrollbar.config(command=lista_box.yview)

# ================= FRAME AÇÕES =================
frame_acoes = tk.Frame(janela, pady=10)
frame_acoes.pack()

tk.Button(frame_acoes, text="Remover Selecionado", width=20, command=remover)\
    .pack()

janela.mainloop()
