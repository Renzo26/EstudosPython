# Onde iremos armazenar os clientes
clientes = {}

print("BEM VINDO AO SISTEMA DE CADASTRO DE CLIENTES POR CPF:\n")

# Fluxo Principal (laço que mantém o programa rodando até o usuário escolher “4 - Sair”)
while True:
    # Exibe o menu principal
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Cadastrar novo cliente")
    print("2 - Consultar cliente por CPF")
    print("3 - Listar todos os CPFs cadastrados")
    print("4 - Sair")

    # Lê a opção do usuário
    opcao = input("Escolha uma opção: ")

    # Opção 1 - Cadastrar novo cliente
    if opcao == "1":
        try:
            cpf = int(input("Digite o CPF para ser cadastrado (somente números): "))
            if cpf in clientes:
                print("CPF já cadastrado.")
            else:
                nome = input("Digite o nome completo: ")
                cep = input("Digite o CEP: ")
                # Armazena no dicionário com as chaves corretas
                clientes[cpf] = {
                    "nome": nome,
                    "cep": cep
                }
                print("Cadastro realizado com sucesso!")
        except ValueError:
            print("CPF inválido! Digite apenas números.")

    # Opção 2 - Consultar cliente por CPF
    elif opcao == "2":
        try:
            cpf = int(input("Digite o CPF a ser consultado: "))
            if cpf in clientes:
                # Acessa o dicionário corretamente
                print(f"\nNOME: {clientes[cpf]['nome']}")
                print(f"CEP: {clientes[cpf]['cep']}")
            else:
                print("CPF não encontrado.")
        except ValueError:
            print("CPF inválido! Digite apenas números.")

    # Opção 3 - Listar todos os CPFs cadastrados
    elif opcao == "3":
        if not clientes:
            print("Nenhum cliente cadastrado ainda. Cadastre ao menos um cliente.")
        else:
            print("\n====== CPFs CADASTRADOS ======")
            for cpf, dados in clientes.items():
                # Exibe CPF, nome e CEP de cada entrada
                print(f"CPF: {cpf} | Nome: {dados['nome']} | CEP: {dados['cep']}")

    # Opção 4 - Sair do sistema
    elif opcao == "4":
        print("Encerrando o sistema. Até logo!")
        break  # Sai do while True, encerrando o programa

    # Qualquer outra opção inválida
    else:
        print("Opção inválida. Tente novamente.")
