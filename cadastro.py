
import re

usuarios = []

blocklist = [
    '00000000000',
    '11111111111',
    '22222222222',
    '33333333333',
    '44444444444',
    '55555555555',
    '66666666666',
    '77777777777',
    '88888888888',
    '99999999999'
]

def menu_principal():
    while True:
        print("\n*** MENU ***")
        print("\nEscolha uma opção:")
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("3. Fazer login")
        print("4. Alterar senha")
        print("5. Alterar dados cadastrais")
        print("6. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            cadastrar_usuario()
            opcao()
        elif escolha == '2':
            listar_usuarios()
            opcao()
        elif escolha == '3':
            usuario_logado = fazer_login()
            opcao()
        elif escolha == '4':
            alterar_senha(usuario_logado)
            opcao()
        elif escolha == '5':
            alterar_dados_cadastrais(usuario_logado)
            opcao()
        elif escolha == '6':
            print("Sessão finalizada!")
            break
        else:
            print("Opção inválida. Tente novamente.")

