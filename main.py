import Eliana, Renato, Mateus

while True:
    while True:
        try:
            n1 = float(input('Dgite o primeiro numero: '))
            break
        except ValueError:
            print('Digite um valor válido')

    while True:        
        try:
            n2 = float(input('Dgite o segundo numero: '))
            break
        except ValueError:
            print('Digite um valor válido') 

    
    while True:
        op = int(input('\n1 - soma\n2 - subtração\n3 - divisão\n4 - multiplicação\n5 - raiz quadrada\n'))
        if op == 1:
            print('O resultado da soma é: ', Eliana.soma(n1, n2))
            break
        elif op == 2:
            print('O resultado da subtração é: ', Renato.menos(n1, n2))
            break
        elif op == 3:
            print('O resultado da divisão é: ', Renato.divisao(n1, n2))
            break
        elif op == 4:
            print('O resultado da multiplicação é: ', Eliana.multiplicacao(n1, n2))
            break
        elif op == 5:
                    print('\nO resultado da Raiz Quadrada é: ', Mateus.raiz(n1, n2))
                    break
        else:
            print('Operação inválida')
            break
    print()
 

        
           
       