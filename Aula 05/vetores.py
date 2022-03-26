vetor1, vetor2, vetor_diferenca, vetor_soma, vetor_multiplicacao = [], [], [], [], []
for i in range(3):
    vetor1.append(int(input(f"Digite o {i + 1}º número do vetor 1: ")))
    vetor2.append(int(input(f"Digite o {i + 1}º número do vetor 2: ")))
    vetor_diferenca.append(vetor1[i] - vetor2[i])
    vetor_soma.append(vetor1[i] + vetor2[i])
    vetor_multiplicacao.append(vetor1[i] * vetor2[i])

print(f"Vetor 1: {vetor1}")
print(f"Vetor 2: {vetor2}")
print(f"Vetor Diferença: {vetor_diferenca}")
print(f"Vetor Soma: {vetor_soma}")
print(f"Vetor Multiplicação: {vetor_multiplicacao}")
