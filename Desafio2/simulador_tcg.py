#print("Hello World")

#Entrada de dados e tipos

#monstro1
nome_monstro1 = str(input("Diga o nome do monstro 1: "))
health_points_monstro1 = int(input("Diga os pontos de vida do Monstro 1: "))
damage_points_monstro1 = int(input("Diga os pontos de ataque do Monstro 1: "))

#monstro2
nome_monstro2 = str(input("Diga o nome do monstro 2: "))
health_points_monstro2 = int(input("Diga os pontos de vida do Monstro 2: "))
damage_points_monstro2 = int(input("Diga os pontos de ataque do Monstro 2: "))

################################################################################################################

#Validação de dados

validacao_entrada = [health_points_monstro2, health_points_monstro1, damage_points_monstro1, damage_points_monstro2]
for i in validacao_entrada:
    if i <= 0:
        print("Não são permitidos valores negativos ou zero para os pontos de vida ou ataque dos monstros. Tente de novo.")
        exit()
print(" ")
print("Valores salvos! Bom jogo.")
print(" ")
#################################################################################################################

#Criando as funções

def atacar(nome_atacante, ataque, nome_defensor, hp_defensor):
    hp_defensor = hp_defensor - ataque
    print(f"{nome_atacante} atacou {nome_defensor} causando {ataque} de dano!")
    print(" ")
    return (hp_defensor)

def exibir_placar(nome_1, hp1, nome_2, hp2):
    if hp1 <0:
        hp1 = 0
    if hp2 <0:
        hp2 = 0
    print(f"O monstro {nome_1} está com {hp1} de vida")
    print(f"O monstro {nome_2} está com {hp2} de vida")
    print(" ")
    #essa função retorna none se você pedir o valor

##################################################################################################################

contador_turnos = 1

while health_points_monstro1 and health_points_monstro2 >0:
    print(f"Turno {contador_turnos}, boa sorte aos monstros!")
    print(" ")
    health_points_monstro2 = atacar(nome_monstro1, damage_points_monstro1, nome_monstro2, health_points_monstro2)
    if health_points_monstro2 >0:
        health_points_monstro1 = atacar(nome_monstro2, damage_points_monstro2, nome_monstro1, health_points_monstro1)
    exibir_placar(nome_monstro1, health_points_monstro1, nome_monstro2, health_points_monstro2)
    contador_turnos = contador_turnos + 1

##################################################################################################################

if health_points_monstro1 <=0:
    print(f"O monstro {nome_monstro2} é o vencedor")
else:
    print(f"O monstro {nome_monstro1} é o vencedor!")