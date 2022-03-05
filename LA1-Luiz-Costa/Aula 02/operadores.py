'''
Operadores aritmétricos

Os operadores aritmétricos são utilizados para executar as operações que a sua aplicação utilizar para gerar um resultado


Básicos:
    * Adição: +
    * Subtração: -
    *Divisão: /
    * Divisão Inteira: //
    * Multiplicação: *
    *Módulo: % (Resto da divisão)
    * Exponenciação: **

Atribuição:
     * X += 3 -> x = x + 3
     * X -= 3 -> x = x - 3
     * X /= 3 -> x = x / 3
     * X //= 3 -> x = // 3
     * X *= 3 -> x = x * 3
     * X **= 3 -> x = x ** 3
     * X %= 3 -> x = x % 3

     Precedencia de Operadores:
     1. () -> Agrupamento
     2. ** -> Exponenciação
     3. *, /, %, // -> Multiplicação, divisão, resto e divisão inteira
     4. +, - -> Soma e subtração
'''

n1, n2 = 8, 6
media = (n1 + n2) / 2
teste = 8 * 2 / 3
print(media)
print(f'O valor da variavel teste é:> {teste:.3f}')