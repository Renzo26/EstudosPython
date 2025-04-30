#Calculadora de Notas com Múltiplos Alunos

print("Bem-vindo ao sistema de cálculo de médias!\n")

alunos = {}

for i in range(1, 4):
    entrada = input(f"Digite o nome e as 3 notas do aluno {i}, separadas por espaço: ")
    dados = entrada.split() #SEPARA A STRING EM PARTES A PARTIR DOS ESPAÇOS E CRIA UM TUPLE CHAMADO DADOS
    nome = dados[0] #DEFINE QUE O NOME É A POSIÇÃO 0 DA LISTA DADOS
    notas = list(map(float, dados[1:])) #PEGA A POSIÇÃO 1 QUE É AS NOTAS DA LISTA DADOS E TRANSFORMA TODOS OS INTES DA LISTA EM FLOAT E CRIA UMA LISTA CHAMADO NOTA SO COM AS NOTAS
    media = sum(notas) / 3 #SOMA TODAS AS NOTAS DA LISTA NOTAS E DIVIDE POR 3
    alunos[nome] = media # SALVA NO DICIONÁRIO ALUNOS O NOME = MEDIA

print("\n----- Resultado das Médias -----")
for nome, media in alunos.items(): #. items retorna pares de chaves e valor/ 
    print(f"A média do aluno {nome} é {media:.1f}")

    if media >= 6:
        print(f"Aluno {nome} Aprovado.")
    elif media >= 5:
        print(f"Aluno {nome} está de Recuperação.")
    else:
        print(f"Aluno {nome} Reprovado.")


print(alunos)
print(notas)
