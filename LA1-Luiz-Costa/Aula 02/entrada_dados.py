'''
Em python, podemos obter as informações do usuario através da função input().

'''

nome = input('Digite o seu nome: ')
print(nome)

# Type Casting - Convertendo os tipos de dados em tempo de execução
idade = int(input('Digite a sua idade: '))
ano_nascimento = 2022 - idade
print(ano_nascimento)

# Outros Casts
a = str(3) # '3'
b = int('3') # 3
c = float('3') # 3.0