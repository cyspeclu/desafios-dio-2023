from re import M
import textwrap
def menu():
    menu = """\n
    ======================== MENU ========================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuario
    [q]\tSair
    
    =>"""

    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n=== DEPOSITO REALIZADO COM SUCESSO ===")
    else:
        print("\n=== OPERACAO FALHOU - VALOR INFORMANDO EH INVALIDO! ===")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n=== OPERACAO FALHOU - SALDO INSUFICIENTE! ===")
    
    elif excedeu_limite:
        print("\n=== OPERACAO FALHOU - VALOR DE SAQUE EXCEDE O LIMITE! ===")

    elif excedeu_saques:
        print("\n=== OPERACAO FALHOU - NUMERO MAXIMO DE SAQUES EXCEDIDOS! ===")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"SAQUE:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== SAQUE REALIZADO COM SUCESSO ===")

    else:
        print("\n=== OPERACAO FALHOU - VALOR INFORMADO EH INVALIDO ===")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================== EXTRATO ==================")
    print("NAO FORAM REALIZADAS MOVIMENTACOES" if not extrato else extrato)
    print(f"\nSALDO:\t\tR$ {saldo:.2f}")
    print("================================================")
    
def criar_usuario(usuarios):
    cpf = input("INFORME SEU CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n================== JA EXISTE UM USUARIO COM ESSE CPF! ==================")
        return
    nome = input("INFORME O NOME COMPLETO: ")
    data_nascimento = input("INFORME A DATA DE NASCIMENTO (DD-MM-AAAA)")
    endereco = input("INFORME O ENDERECO: ")
    usuarios.append({"nome": nome, "data_nascimento":data_nascimento, "cpf": cpf, "endereco": endereco})
    print("USUARIO CRIADO COM SUCESSO!")
                 
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("INFORME SEU CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\nCONTA CRIADA COM SUCESSO!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario":usuario}
    print("\nUSUARIO NAO ENCONTRADO")
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agencia:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    numero_saques = 0
    usuarios = []
    contas = []
    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Infomre o valor do deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

        elif opcao == "nc":
            criar_usuario(usuarios)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break
        else:
            print("Operacao invalida, por favor selecione novamente a operacao desejada.")


main()
