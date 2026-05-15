#print("Hello, World")

# 1. Entrada de dados e tipos:

orcamento_reais = float(input("Diga qual é seu orçamento, em reais:"))
destino = str(input("Diga qual seu destino:"))
custo_passagem_reais = float(input("Diga quanto custou sua passagem, em reais:"))
hospedagem_dia_reais = float(input("Diga o custo diário da hospedagem, em reais:"))
print("Quase lá! Diga a duração de sua viagem, em dias:")
tempo_dias = int(input())

# 1.1 Exceção

lista_testar = [orcamento_reais, custo_passagem_reais, hospedagem_dia_reais, tempo_dias]
for i in range(3):
    if lista_testar[i]<0:
        print("Não são aceitos valores negativos")
        quit()
    else:
        continue
    i=i+1


# 2. Cálculos e Lógica

orcamento_euros = orcamento_reais * 6.1
custo_passagem_euros = custo_passagem_reais * 6.1
hospedagem_dia_euros = hospedagem_dia_reais * 6.1
print(f"Em euros, seu orçamento é {orcamento_euros}, sua passagem foi {custo_passagem_euros} e sua diária é {hospedagem_dia_euros}.")

custo_hospedagem_euros = hospedagem_dia_euros * tempo_dias
print(f"Seu custo total com hospedagem é {custo_hospedagem_euros} euros.")
custo_hospedagem_reais = hospedagem_dia_reais * tempo_dias

custo_total_euros = custo_passagem_euros + custo_hospedagem_euros
print(f"Prepara o coração! O custo total da sua viagem é {custo_total_euros} euros!")
custo_total_reais = custo_passagem_reais + custo_hospedagem_reais
print(f"Se você não entende nada de euro... O custo total da sua viagem é {custo_total_reais} reais!")

if custo_total_euros <= orcamento_euros:
    print("Sua viagem tem orçamento possível")
else:
    print("Sua viagem tem orçamento impossível")

if custo_total_euros<=orcamento_euros and tempo_dias>0:
    viável = True
    print(f"Sua viagem é viável. Sobrará {orcamento_euros-custo_total_euros} euros, compre um presente pra mim!")
else:
    viável = False
    print(f"Sua viagem é inviável. Falta {abs(orcamento_euros-custo_total_euros)} euros, fale com um agiota.")


