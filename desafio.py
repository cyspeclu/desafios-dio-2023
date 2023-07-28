menu = """
    =================== MENU ===================
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [q] - Sair

Informe sua opcao:
"""

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    opcao = str(input(menu).lower())
    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operacao falhou.. O valor informado eh invalido!")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_de_saques >= LIMITE_DE_SAQUES

        if excedeu_saldo:
            print("Operacao falhou... Saldo insuficiente!")

        elif excedeu_limite:
            print("Operacao falhou... Valor do saque excede o limite!")
        
        elif excedeu_saque:
            print("Operacao falhou... Saques excedidos!")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
    elif opcao == "e":
        print("\n=================== EXTRATO ===================")
        print("Movimentacoes nao foram realizadas." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("==================================================")
    elif opcao == "q":
        print("Ate mais...")
        break
    else:
        print("Operacao invalida, tente novamente...")
