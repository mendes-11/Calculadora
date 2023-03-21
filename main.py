import Eliana, Renato, mateus

while True:
    try:
        n1 = float(input('Digite o primeiro numero:\n'))
    except ValueError:
        print('Digite um valor válido')
    
    try:
        n2 = float(input('Digite o segundo numero:\n'))
    except ValueError:
        print('Digite um valor válido') 

    op = int(input('''
1 - Soma
2 - Subtração
3 - Divisão
4 - Multiplicação
5 - Raiz Quadrada\n'''))

    while True:
        if op == 1:
            print('\nO resultado da soma é: ', Eliana.soma(n1, n2))
            break
        elif op == 2:
            print('\nO resultado da subtração é: ', Renato.menos(n1, n2))
            break
        elif op == 3:
            print('\nO resultado da divisão é: ', Renato.divisao(n1, n2))
            break
        elif op == 4:
            print('\nO resultado da multiplicação é: ', Eliana.multiplicacao(n1, n2))
            break
        elif op == 5:
            print('\nO resultado da Raiz Quadrada é: ', mateus.raiz(n1, n2))
            break
        else:
            print('Operação inválida')
            break
    
    fe = input("\nDigite 0 se quiser sair ou qualque coisa para continuar:\n")
    
    if fe == '0':
        break

        
           
       