## Challenge: Creating a Banking System - Part 02

### Creating the Menu

- Create the Menu Function to display the options for the user:

```python
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
```

---

### Creating the "Deposit" function

1. Defining a function called depositar.

2. It takes 3 things:

    1. Saldo

    2. Deposito

    3. Extrato

3. We need to check if the "Deposito" > 0, because you cannot deposit negative amounts in your account.

4. In order to register this deposit, we need to add it to the "saldo" (your current balance).

```python
def depositar(saldo, deposito, extrato, /):
    if deposito > 0:
        saldo += deposito
        extrato += f"Deposito:\tR$ {deposito} \n"
        print("\n ==== Depósito realizado com sucesso. ====")
    else:
        print("!!!! Operação falhou. Valor inválido. !!!!")

    return saldo, extrato
```

---

### Creating "Sacar" function

1. This function will control when you need to withdraw some money

2. This function call a lot of arguments:

    1. Saldo (balance)

    2. Saque (withdraw value)

    3. Extrato (register of transactions)

    4. Limite (how much you can withdraw)

    5. Numero_saques (count the number of withdraws)

    6. Limite_saques (how many withdraws you can do)

3. First of all, we will check the limits

4. Then, we will print messages for each situation

5. Then, after pass for every limit, we can wihdraw.

    1. We need to register it, updating the "Saldo" (current balance)

    2. Printing the operationg in the "Extrato" (register of all transactions)

    3. Updating the "numero_saques" (count the number of withraws)

```python
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
```

---

### Creating "Exibe_extrato" function

- A function to show the transaction history

```python
def exibe_extrato(saldo,/, *, extrato):
    print(" =========== EXTRATO ============ \n")
    if extrato == "":
        print("Não foram realizadas movimentações")
    else:
        print(extrato)
        print(f"Saldo atual: R$ {saldo}")
    
    print("=================================")
```

---

### Creating "Criar_usuario" and "filter_usuario" functions

1. This function will create nuw users for our system.

2. It begins with the number of the "cpf" (cadastro de pessoa física - a unique number that brazilian people has to indentify)

3. Then we will call a function "filter_usar" to check if this user is already in the system.

4. It there isn't any user with this "cpf", then we register:

    1. Name

    2. Birthdate

    3. Address

5. Then, append all this information in the "usuarios" list, as a dictionary.

```python
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
```

---

### Creating "criar_conta" function

1. All users need to open an account after they are registered in the system.

2. First of all, we need to check if the user is really registered in the system.

3. Then, we create an account.

### Creating "listar_contas" function

1. A function to list all the accounts in the system.

```python
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
    print("="*50)
    print(textwrap.dedent(linha))
```

---

### MAIN function

1. Defining the variables and constants:

    1. LIMITE_SAQUES (how many withdraws someone can do)

    2. AGENCIA (This bank only has one Agency)

    3. Saldo = 0 (the balance starts with $ 0)

    4. limite = 500 (limit for each withdraw)

    5. extrato = "" (transaction history)

    6. numero_saques = 0 (count the number of withdraws)

    7. usuarios = [] (empty list with the users)

    8. contas = [] (empty list with the bank accounts)

2. The we will call each function that we defined earlier

```python
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
```

---

### Considerations

- The solution followed all the constraints imposed by the problem.

- The system is still incomplete and will be implemented later.

- Withdrawals and deposits are not yet linked to any specific user.

- This challenge helped in the implementation of functions, loops, variable definitions, scopes, and various other concepts in Python.

