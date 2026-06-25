num1 = 0
num2 = 0

def pegar_numeros():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    return num1, num2

opcao = "None"
while opcao != '0':
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        num1, num2 = pegar_numeros()
        resposta = num1 + num2
        print(f'A soma de {num1} + {num2} é: {resposta}')
        
    elif opcao == '2':
        num1, num2 = pegar_numeros()
        resposta = num1 - num2
        print(f'A subtração de {num1} - {num2} é: {resposta}')

    elif opcao == '3':
        num1, num2 = pegar_numeros()
        resposta = num1 * num2
        print(f'A multiplicação de {num1} * {num2} é: {resposta}')

    elif opcao == '4':
        num1, num2 = pegar_numeros()
        resposta = num1 / num2
        print(f'A divisão de {num1} / {num2} é: {resposta}')
        
    elif opcao == '0':
        print("Saindo do programa...")
        
    else:
        print("Opção inválida! Tente novamente....")
        
    
    
    