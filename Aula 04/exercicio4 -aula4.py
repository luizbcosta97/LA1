'''Faça um script utilizando o for, que permita ao usuário fazer três contas de subtração. Para isso peça ao usuário dois números 
a cada iteração do loop e mostre na tela o resultado da operação.

Entrada:
1
2
4
3
9
5

Saída:
1 - 2 = -1
4 - 3 = 1
9 - 5 = 4
'''



# range(3) -> [0, 1, 2]
for i in range(3):
    numero1 = int(input("Digite um número1: "))
    numero2 = int(input("Digite um número2: "))
    resultado = numero1 - numero2
    print(resultado)
        



    

