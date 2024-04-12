import textwrap

def menu():
    menu = """
        =========== Menu ===========

        [d]\t Depositar
        [s]\t Sacar
        [e]\t Extrato
        [nc]\t Nova Conta
        [lc]\t Listar contas
        [nu]\t Novo usuário
        [q]\t Sair

        => """
    return input(textwrap.dedent(menu))

def depositar(saldo, deposito, extrato, /):
    if deposito > 0:
        saldo += deposito
        extrato += f"Deposito:\tR$ {deposito} \n"
        print("\n ==== Depósito realizado com sucesso. ====")
    else:
        print("!!!! Operação falhou. Valor inválido. !!!!")

    return saldo, extrato

def sacar(*, saldo, saque, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = saque > saldo
    excedeu_limite = saque > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("!!! Você nao tem saldo suficiente. """)
    
    elif excedeu_limite:
        print("!!! O valor solicitado excele o seu limite. !!!")
    
    elif excedeu_saques:
        print("!!! Número máximo de saques excedido. !!!")

    elif saque > 0:
        saldo -= saque
        extrato += f"Saque:\t\tR$ {saque:.2f}\n"
        numero_saques += 1
        print("==== Saque realizado com sucesso ====")
    
    else:
        print("!!! Valor inválido para saque. !!!")

    return saldo, extrato, numero_saques

def exibe_extrato(saldo,/, *, extrato):
    print(" =========== EXTRATO ============ \n")
    if extrato == "":
        print("Não foram realizadas movimentações")
    else:
        print(extrato)
        print(f"Saldo atual: R$ {saldo}")
    
    print("=================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filter_usuario(cpf, usuarios)

    if usuario:
        print("\n !!! Já existe usuário com este CPF !!!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereco (rua, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("==== Usuário criado com sucesso! ====")

def filter_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filter_usuario(cpf, usuarios)

    if usuario:
        print("\n ===== Conta criada com sucesso! ====")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("!!!! Usuário não encontrado, não foi possível criar a conta !!!!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
    print("="*50)
    print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            deposito = float(input("Valor a depositar: "))

            saldo, extrato = depositar(saldo, deposito, extrato)
        
        elif opcao == "s":
            
            saque = float(input("Valor do saque: "))
            
            saldo, extrato, numero_saques = sacar(
                saldo = saldo,
                saque = saque,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES
            )

        elif opcao == "e":
            exibe_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()