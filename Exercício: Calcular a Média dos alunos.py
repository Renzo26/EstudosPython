#Calculadora de Notas com Múltiplos Alunos

print("Bem-vindo ao sistema de cálculo de médias!\n")

alunos = {}

for i in range(1, 4):
    entrada = input(f"Digite o nome e as 3 notas do aluno {i}, separadas por espaço: ")
    dados = entrada.split()
    nome = dados[0]
    notas = list(map(float, dados[1:]))
    media = sum(notas) / 3
    alunos[nome] = media

print("\n----- Resultado das Médias -----")
for nome, media in alunos.items():
    print(f"A média do aluno {nome} é {media:.1f}")

    if media >= 6:
        print(f"Aluno {nome} Aprovado.")
    elif media >= 5:
        print(f"Aluno {nome} está de Recuperação.")
    else:
        print(f"Aluno {nome} Reprovado.")


print(alunos)
