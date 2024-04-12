
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("################ Depósito ################")
        deposito = float(input("Valor a depositar: "))
        saldo += deposito
        extrato += f" Deposito de R$ {deposito} \n"
    
    elif opcao == "s":
        print("################ Saque ################")
        if saldo == 0:
            print("Não é possível sacar, pois o saldo é 0 (zero)")
        elif LIMITE_SAQUES == 0:
            print("Limites de saques do dia atingido. Retorne amanhã.")
        else:
            saque = float(input("Valor do saque: "))
            if saque > saldo:
                print(f"Você não pode sacar esta quantia. Seu saldo é de R$ {saldo}")
            elif saque >= 500:
                print("O limite por saque é de R$ 500,00.")
            else:
                saldo -= saque
                LIMITE_SAQUES -=1
                extrato += f" Saque de R$ {saque} \n"

    elif opcao == "e":
        print("################ Extrato ################")
        if extrato == "":
            print("Não foram realizadas movimentações")
        else:
            print(extrato)
            print(f"Saldo atual: R$ {saldo}")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")