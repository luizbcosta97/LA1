'''Escreva um programa que declare uma váriavel numero, inicialize-a com 0, e incremente-a de 1000 em 1000, mostrando seu valor na tela, ate que seu valor seja 100000 (cem mil)
'''

i: int = 0
while i < 100000:
    print(f"Resultado{i + 1000}")
    i += 1000
