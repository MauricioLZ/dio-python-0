def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

LIMITE_SAQUE = 500
LIMITE_N_SAQUES = 3

saldo = 0
n_saques = 0
extrato = ""

menu = f"""Selecione uma operação:
[d] = deposito
[s] = saque
[e] = extrato
[f] = fechar
"""

while True:

    print(f"\n\nSaldo atual: R${saldo: .2f}")
    opcao = input(menu)

    if opcao == "d":
        print("\nDepósito")
        valor_str = input("Valor a ser depositado: ")
        valor = float(valor_str) if is_float(valor_str) else -1

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R${valor: .2f}\n"
            print(f"R${valor: .2f} depositado com sucesso.")

        else:
            print("Valor inválido.")

    elif opcao == "s":
        if n_saques >= LIMITE_N_SAQUES:
            print(f"\nVocê atingiu seu limite de {n_saques} saques diários.")
        
        else:
            print("\nSaque")
            valor_str = input("Valor a ser sacado: ")
            valor = float(valor_str) if is_float(valor_str) else -1

            if valor > 0 and valor <= LIMITE_SAQUE and valor <= saldo and n_saques < LIMITE_N_SAQUES:
                saldo -= valor
                n_saques += 1
                extrato += f"Saque de R${valor: .2f}\n"
                print(f"R${valor: .2f} sacado com sucesso.")

            elif valor < 0:
                print("Valor inválido.")

            elif valor > saldo:
                print(f"Saldo insuficiente. Saldo atual: R${saldo: .2f}.")

            elif valor > LIMITE_SAQUE:
                print(f"O valor máximo de saque permitido é de R${LIMITE_SAQUE: .2f}.")

    elif opcao == "e":
        print(f"\nExtrato:\n{extrato}")

    elif opcao == "f":
        print("\nObrigado por utilizar nossos serviços!")
        break

    else:
        print("Operação inválida")