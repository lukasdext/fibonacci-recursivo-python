opcao = 's'

while opcao == 's':
    def Fibonacci(n):

    # Sequencia Fibonacci: 0 1 1 2 3 5 8 13 21 34 55 89
    #           POSIÇÃO  : 0 1 2 3 4 5 6 7  8  9  10 11

            if n < 0:
                print("Incorrect input")
        
            
            elif n == 0:
                return 0
        
        
            elif n == 1 or n == 2:
                return 1
        
            else:
                return Fibonacci(n-1) + Fibonacci(n-2)
        
    n = int(input("Digite um numero:  "))
    res = Fibonacci(n)
    print('Na POSIÇAO %d o valor é %d' % (n, res))
    opcao =input("Deseja voltar ao menu principal ? (s/n)").lower()


