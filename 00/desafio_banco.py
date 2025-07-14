
print("Escolha uma opção:")
print("[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair")

menu = ''
saldo = 0
limite = 500.00
extrato = []
numero_saques = 0
limite_saques = 3


while True:
    
    opcao = input(menu)
    print("\n======================\n")
    
    if opcao == "d":
        
        print("Depósito")
        valor = float(input(print("Valor para depósito: ")))
        saldo +=valor
        extrato.append("Depósito: R$" + str(valor))
        print(f"Valor depositado: R${valor:.2f}, Saldo:R${saldo:.2f}")
        print("\n======================\n")

    elif opcao == "s":
        print("Saque")
        
        if limite_saques > 0:
            
            valor = float(input(print("Valor para saque: ")))
            
            while valor > limite:
                valor = float(input(print("Valor do saque excede o limite, digite um novo valor: ")))

            limite_saques -= 1
            saldo -= valor
            extrato.append("Saque: -R$"+ str(valor))
            print(f"Valor sacado R${valor:.2f}, Saldo:R${saldo:.2f}")
            print("\n======================\n")
        else:
            print("Limite de saques excedido")
            print("\n======================\n")


    elif opcao == "e":
        print("Extrato")
        if extrato == "":
            print("Não foram realizadas movimentações na conta.")
            print("\n======================\n")
        else:
            for valor in extrato:
                print(valor) 
        print("Saldo: R$",saldo)        
        print("\n======================\n")        

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")