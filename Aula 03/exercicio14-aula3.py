'''
Leia o salario de um trabalhador e o valor da prestação de um empréstimo. 
Se a prestaçao for maior que 20% do salário imprima: “empréstimo não concedido”, caso contrario imprima: “empréstimo concedido”.
'''

salario = float(input("Digite o seu salario: "))
valor_prestacao = float(input("Digite o valor da prestação: "))

if valor_prestacao > salario * 0.2: 
    print("Emprestimo não concedido")
else: 
    print("Emprestimo concedido")
        