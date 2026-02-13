import json
import os


def mostrar_menu():
    print("\n=== Sistema de Cadastro de Usuários ===")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("0 - Sair")


def carregar_usuarios():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    else:
        return []


def salvar_usuarios(lista_usuarios):
    with open("usuarios.json", "w", encoding="utf-8") as arquivo:
        json.dump(lista_usuarios, arquivo, ensure_ascii=False, indent=4)


def cadastrar_usuario(lista_usuarios):
    nome = input("Digite o nome do usuário: ")

    if nome.strip() == "":
        print("Nome inválido. Cadastro cancelado.")
        return

    lista_usuarios.append(nome)
    salvar_usuarios(lista_usuarios)
    print("Usuário cadastrado com sucesso!")


def listar_usuarios(lista_usuarios):
    if len(lista_usuarios) == 0:
        print("Nenhum usuário cadastrado.")
        return

    print("\nUsuários cadastrados:")
    for indice, nome in enumerate(lista_usuarios, start=1):
        print(f"{indice} - {nome}")


def main():
    usuarios = carregar_usuarios()
    opcao = ""

    while opcao != "0":
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario(usuarios)
        elif opcao == "2":
            listar_usuarios(usuarios)
        elif opcao == "0":
            print("Saindo do sistema...")
        else:
            print("Opção inválida.")


main()
