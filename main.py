import Eliana, Renato

while True:
    
    try:
        n1 = float(input('Dgite o primeiro numero: '))
    except ValueError:
        print('Digite um valor válido')
    try:
        n2 = float(input('Dgite o segundo numero: '))

    except ValueError:
        print('Digite um valor válido') 
        
    op = ('\n1 - soma\n2 - subtração\n 3 - divisão\n4 - multiplicação')
    while True:
        if op == 1:
            soma(n1, n2)
            print('O resultado da soma é: ', soma)
            break
        elif op == 2:
            menos(n1, n2)
            print('O resultado da subtração é: ', menos)
            break
        elif op == 3:
            divisao(n1, n2)
            print('O resultado da divisão é: ', divisao)
            break
        elif op == 4:
            muliplicaao(n1, n2)
            print('O resultado da multiplicação é: ', multiplicaao)
            break
        else:
            print('Operação inválida')
    
    break

        
           
       