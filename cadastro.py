
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
def cadastrar_usuario():
    print("\n***CADASTRO DE USUÁRIO***")
    def validar_cpf_2(cpf):

        corpo_cpf = cpf[:9]
        digito_cpf = cpf[-2:]

        calculo_1 = 0
        calculo_2 = 0

        multiplicacao = [10, 9, 8, 7, 6, 5, 4, 3, 2]

        for i, j in zip(multiplicacao, corpo_cpf):
            calculo_1 += i * int(j)
    

        resto_1 = calculo_1 % 11
   

        digito_1 = 0 if resto_1 < 2 else 11 - resto_1
   

        corpo_cpf += str(digito_1)

        for i, j in zip(multiplicacao, corpo_cpf[1:]):
            calculo_2 += i * int(j)

  

        resto_2 = calculo_2 % 11
    

        digito_2 = 0 if resto_2 < 2 else 11 - resto_2
   

        return digito_cpf == f'{digito_1}{digito_2}'

    while True:
        nome = input("Digite seu nome: ")
        if nome.replace(" ", "").isalpha():
            break
        else:
            print("O nome não pode conter números ou estar vazio. Tente novamente.")


    email = input("Digite seu e-mail: ")

    verificar_email = False

    for usuario in usuarios:
        if usuario['email'] == email:
            verificar_email = True
            break

    if verificar_email:
        print("Este e-mail já está cadastrado. Acesse a página de login")
        return

    else:
        while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("E-mail inválido. Deve conter '@' e '.'.")
            email = input("Digite seu e-mail novamente: ")           

    cpf = input("Informe seu CPF: ")

    verificar_cpf = False

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            verificar_cpf = True
            break

    if verificar_cpf:
            print("Este CPF já está cadastrado. Acesse a página de login.")
            return
    else:

        while True:
            cpf_sem_ponto = cpf.replace('.', '')
            cpf = cpf_sem_ponto.replace('-', '')

            if cpf.replace(" ","").isnumeric():

                if len(cpf) == 11:

                    if cpf in blocklist:

                        cpf = input('> O CPF não pode ter todos os números iguais! Digite novamente: \n')

                    else:

                        if validar_cpf_2(cpf):
                            print('CPF Válido!\n')
                            break

                        else:
                            cpf = input(' CPF Inválido! Digite novamente seu CPF: \n')

                else:
                     cpf = input('> O número de CPF deve ter 11 dígitos! Digite novamente seu CPF: \n')
            else:
                cpf = input('> O campo CPF é obrigatório. Digite seu CPF: \n')

    senha = input("Crie sua senha. A senha deve ter 8 posições e conter letras e números: ")
    while not (any(char.isalpha() for char in senha) and any(char.isdigit() for char in senha) and len(senha) == 8):
        print("\n***Senha fora do padrão! tente novamente abaixo.***")
        senha = input("\nCrie sua senha com 8 digitos devendo conter letras e números: ")

    confirmar_senha = input("Confirme sua senha: ")
    while senha != confirmar_senha:
        print("As senhas não coincidem. Tente novamente.")
        confirmar_senha = input("Confirme sua senha novamente: ")

    tem_convenio = input("Possui algum plano de saúde? \n0 - Sim\n1 - Não\n")

    while not (tem_convenio == "0" or tem_convenio == "1"):
        tem_convenio = input("opção inválida! Digite '0' caso tenha um plano de saúde ou digite '1' se não possuir.\n" )
    if tem_convenio == "0":
        convenio = "sim"
        print("Digite a opção correspondente ao nome do seu Plano de Saúde:\n1 - Amil\n2 - Sulamerica\n3 - NotreDame Intermedica\n4 - Bradesco\n5 - Hapvida\n6 - Unimed\n7 - Outro")

        plano_de_saude = input("")

        while not plano_de_saude in ["1", "2", "3", "4", "5", "6","7"]:
            plano_de_saude = input("opção inválida! Tente novamente.\n")

        if plano_de_saude == "1":
            nome_plano = "Amil"
        elif plano_de_saude == "2":
            nome_plano = "Sulamerica"
        elif plano_de_saude == "3":
            nome_plano = "NotreDame Intermedica"
        elif plano_de_saude == "4":
            nome_plano = "Bradesco"
        elif plano_de_saude == "5":
            nome_plano = "Hapvida"
        elif plano_de_saude == "6":
            nome_plano = "Unimed"
        elif plano_de_saude == "7":
            nome_plano = input ("Você selecionou Outro. Digite o nome do seu plano de Saúde: ")

    elif tem_convenio == "1":
        convenio = "não"
        nome_plano = "-"

    no_espectro = input("Tem em seu convívio ou é alguém no espectro autista? \n0 - Sim\n1 - Não\n")

    while not (no_espectro == "0" or no_espectro == "1"):
        no_espectro = input("opção inválida! Digite '0' caso conviva ou esteja no espectro ou digite '1' se não é/conhece.\n" )
    if no_espectro == "0":
        conhece_ou_esta_no_espectro = "sim"

    elif no_espectro == "1":
        conhece_ou_esta_no_espectro = "não"


    usuario = {'nome': nome, 'email': email, 'cpf': cpf, 'senha': senha, 'convenio': convenio, 'plano_saude': nome_plano, 'conhece_ou_esta_no_espectro': conhece_ou_esta_no_espectro}
    usuarios.append(usuario)
    print("\nCadastro realizado com sucesso!\n==============================") 

def listar_usuarios():
    print("\n***USUÁRIOS CADASTRADOS***")

    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, E-mail: {usuario['email']}, CPF: {usuario['cpf']}, Tem Convênio? {usuario['convenio']}, Plano de Saúde: {usuario['plano_saude']}, Conhece ou está no espectro autista: {usuario['conhece_ou_esta_no_espectro']}")
    print()


def fazer_login():
    print("\n***TELA DE LOGIN***")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    for usuario in usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
            print(f"\nLogin realizado com sucesso, bem-vindo {usuario['nome']}!")
            return usuario
    print("\nNão foi possível fazer login. E-mail ou senha incorretos.")


usuario_logado = None

def alterar_senha(usuario_logado):
    print("\n***ALTERAR SENHA***")
    if usuario_logado:
        print(f"Alterar Senha para o usuário {usuario_logado['nome']}")

        while True:
            senha_atual = input("Digite a senha atual: ")
            if senha_atual == usuario_logado['senha']:
                break
            else:
                print("Senha atual incorreta. Tente novamente.")

        while True:
            nova_senha = input("Digite a nova senha: ")
            if any(char.isalpha() for char in nova_senha) and any(char.isdigit() for char in nova_senha) and len(nova_senha) == 8:
                break
            else:
                print("\n**Senha fora do padrão. A senha deve conter letras e números e ter 8 posições. Tente novamente.***")

        while True:
            confirmar_senha = input("Confirme a nova senha: ")
            if nova_senha == confirmar_senha:
                break
            else:
                print("As senhas não coincidem. Tente novamente.")

        usuario_logado['senha'] = nova_senha
        print("Senha alterada com sucesso!")
    else:
        print("Usuário não está logado. Necessário fazer login para alterar a senha.")


usuario_logado = None

def alterar_dados_cadastrais(usuario_logado):
    print("\n***ALTERAR DADOS USUÁRIO***")
    if usuario_logado:
        print("***Alterar Dados Cadastrais***\n")
        print("1. Alterar Nome")
        print("2. Alterar E-mail")
        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            novo_nome = input("Digite o novo nome: ")
            while any(char.isdigit() for char in novo_nome):
                print("O nome não pode conter números.")
                novo_nome = input("Digite o novo nome novamente: ")
            usuario_logado['nome'] = novo_nome
            print("Nome alterado com sucesso!")

        elif escolha == '2':
            novo_email = input("Digite o novo e-mail: ")
            while not re.match(r"[^@]+@[^@]+\.[^@]+", novo_email):
                print("E-mail inválido. Deve conter '@' e '.'.")
                novo_email = input("Digite o novo e-mail novamente: ")
            usuario_logado['email'] = novo_email
            print("\nE-mail alterado com sucesso!")

        else:
            print("\nOpção inválida.")
    else:
        print("\nUsuário não está logado. Necessário fazer login para alterar os dados cadastrais.")

def opcao():
    opcao = input("O que deseja fazer?\n0 - Retornar ao Menu Principal.\n1 - Sair do Sistema.\n")
    while opcao not in ['0','1']:
        opcao = input("Opção inválida. Tente novamente.")
    if opcao == '0':
        print("Retornando ao menu principal...")
    elif opcao == '1':
        print("Encerrando o programa...")
        exit()
menu_principal()



