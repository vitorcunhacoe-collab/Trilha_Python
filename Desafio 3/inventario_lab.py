#print("Hello World")

# Dados do inventário físico (cada índice representa um frasco individual)

reagentes = ['Etanol', 'Acetona', 'Etanol', 'Ácido Sulfúrico', 'Benzeno', 'Acetona','Etanol', 'Ácido Sulfúrico', 'Metanol', 'Tolueno', 'Etanol', 'Acetona', 'Ácido Acético', 'Etanol', 'Benzeno', 'Ácido Sulfúrico', 'Metanol', 'Ácido Acético','Etanol', 'Acetona', 'Tolueno', 'Ácido Sulfúrico', 'Benzeno', 'Etanol', 'Acetona','Metanol', 'Ácido Sulfúrico', 'Acetona', 'Ácido Acético', 'Etanol']
lotes = ['2023-ETA-01', '2023-ACE-01', '2023-ETA-01', '2023-SUL-01','2023-BEN-01', '2024-ACE-01', '2023-ETA-02', '2024-SUL-01', '2023-MET-01','2024-TOL-01', '2023-ETA-01', '2023-ACE-01', '2023-ACA-01', '2023-ETA-02','2023-BEN-01', '2023-SUL-01', '2023-MET-01', '2024-ACA-01', '2023-ETA-01','2023-ACE-01', '2024-TOL-01', '2024-SUL-01', '2023-BEN-01', '2023-ETA-01','2023-ACE-01', '2023-MET-01', '2023-SUL-01', '2024-ACE-01', '2024-ACA-01','2023-ETA-02']
purezas = [99.5, 92.0, 99.5, 98.0, 99.9, 98.5, 96.0, 99.0, 99.0, 98.8, 99.5, 92.0, 99.2, 96.0, 99.9, 98.0, 99.0, 95.0, 99.5, 92.0, 98.8, 99.0, 99.9, 99.5, 92.0, 99.0, 98.0, 98.5, 95.0, 96.0]

# Passo 1: Eliminar duplicatas utilizando set: conjunto sem ordem e sem repetições

reagentes_conjunto = set(reagentes)
#print(reagentes_conjunto)

#Passo 2: Contar quantos são utilizando len: conta quantos elementos existem dentro de uma estrutura de dados

n_reagentes_unicos = len(reagentes_conjunto)
print(f"A quantidade total de reagentes diferentes é {n_reagentes_unicos}")

# Passo 3: Unir as listinhas com zip: descobri que dá pra unir as 3 de uma vez

uniao = zip(reagentes, lotes, purezas)
lista_tuplas = list(uniao)
#print(lista_tuplas)

#Passo 4: Percorrer a lista utilizando o for (meio confuso pra mim)

#for reagente, lote, pureza in lista_tuplas:
#    print(f"Frasco do Lote: {lote} | Reagente: {reagente} | Pureza: {pureza}%")

#Passo 5: Verificar quais purezas são maiores ou iguais a 98%

#Vou fazer primeiro utilizando if normal

#lotes_aprovados = []

#for reagente, lote, pureza in lista_tuplas:
#    print(f"Frasco do Lote: {lote} | Reagente: {reagente} | Pureza: {pureza}%")
#    if pureza >= 98.0:
#        lotes_aprovados.append(lote)

#print(f"Esses são os lotes aprovados para experimentos sensíveis: {lotes_aprovados}")

#deu certo, fazendo com listening comprehension:

lotes_aprovados = [lote for reagente, lote, pureza in lista_tuplas if pureza >= 98.0]
print(f"Esses são os lotes aprovados para experimentos sensíveis: {lotes_aprovados}")