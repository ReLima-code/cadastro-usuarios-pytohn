import json
import os


def mostrar_menu():
    print("\n=== Sistema de Cadastro de Usuários ===")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Remover usuário")
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
    nome = input("Digite o nome do usuário: ").strip()
    email = input("Digite o email do usuário: ").strip()

    if nome == "" or email == "":
        print("Nome ou email inválido. Cadastro cancelado.")
        return
    
    usuario = {
        "nome": nome,
        "email": email
    }

    lista_usuarios.append(usuario)
    salvar_usuarios(lista_usuarios)
    print("Usuário cadastrado com sucesso!")


def listar_usuarios(lista_usuarios):
    if len(lista_usuarios) == 0:
        print("Nenhum usuário cadastrado.")
        return

    print("\nUsuários cadastrados:")
    for indice, usuario in enumerate(lista_usuarios, start=1):
        print(f"{indice} - Nome: {usuario['nome']} | Email: {usuario['email']}")


def remover_usuario(lista_usuarios):
    if len(lista_usuarios) == 0:
        print("Nenhum usário para remover.")
        return
    
    listar_usuarios(lista_usuarios)

    try:
        indice = int(input("Digite o número de usuário que deseja remover: "))

        if 1 <= indice <= len(lista_usuarios):
            usuario_removido = lista_usuarios.pop(indice - 1)
            salvar_usuarios(lista_usuarios)
            print(f"Usuário {usuario_removido['nome']} removido com sucesso!")
        else:
            print("Número invalido.")
    except ValueError:
        print("Digite um número válido.")


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
        elif opcao == "3":
            remover_usuario(usuarios)
        elif opcao == "0":
            print("Saindo do sistema...")
        else:
            print("Opção inválida.")


main()
