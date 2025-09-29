nome_1 = input()
nome_2 = input()
nome_3 = input()

pontos_1 = 0
pontos_2 = 0
pontos_3 = 0

print("Vai começar o esconde-esconde UFPE 2025!")

##// Lista de prédios
predio_1 = "CFCH"
predio_2 = "CTG"
predio_3 = "CIN"


##===== Buscador 1 =====
#CFCH
print()
print("Prontos ou não, lá vai", nome_1+".")
print("Agora",nome_1,"procurará no",predio_1 +".")
entrada = ""
while entrada != "Fim da busca nesse prédio.":
    entrada = input()
    if entrada == "Achou uma pessoa!":
        pontos_1 = pontos_1 + 1
        print(nome_1,"achou uma pessoa!")
        
entrada = ""

#CTG
print("Agora",nome_1,"procurará no",predio_2+".")
while entrada != "Fim da busca nesse prédio.":
    entrada = input()
    if entrada == "Achou uma pessoa!":
        pontos_1 = pontos_1 + 1
        print(nome_1,"achou uma pessoa!")

entrada = ""
#CIN
print("Agora",nome_1,"procurará no",predio_3+".")
while entrada != "Fim da busca nesse prédio.":
    entrada = input()
    if entrada == "Achou uma pessoa!":
        pontos_1 = pontos_1 + 1
        print(nome_1,"achou uma pessoa!")
        
##===== Buscador 2 =====
print()
print("Prontos ou não, lá vai", nome_2+".")
entrada = ""

#CFCH

print("Agora",nome_2,"procurará no",predio_1+".")
entrada = ""
while entrada != "Fim da busca nesse prédio.":
    entrada = input()
    if entrada == "Achou uma pessoa!":
        pontos_2 = pontos_2 + 1
        print(nome_2,"achou uma pessoa!")

#CTG        
print("Agora",nome_2,"procurará no",predio_2+".")
entrada = ""
while entrada != "Fim da busca nesse prédio.":
    entrada = input()
    if entrada == "Achou uma pessoa!":
        pontos_2 = pontos_2 + 1
        print(nome_2,"achou uma pessoa!")

#CIN   
print("Agora",nome_2,"procurará no",predio_3 + ".")
entrada = ""
while entrada != "Fim da busca nesse prédio.":
    entrada = input()
    if entrada == "Achou uma pessoa!":
        pontos_2 = pontos_2 + 1
        print(nome_2,"achou uma pessoa!")
        
##===== Buscador 3 =====        
print()
print("Prontos ou não, lá vai", nome_3+".")
print("Agora",nome_3,"procurará no",predio_1+".")

entrada = ""
while entrada != "Fim da busca nesse prédio.":
    entrada = input()
    if entrada == "Achou uma pessoa!":
        pontos_3 = pontos_3 + 1
        print(nome_3,"achou uma pessoa!")

#CTG        
print("Agora",nome_3,"procurará no",predio_2+".")
entrada = ""
while entrada != "Fim da busca nesse prédio.":
    entrada = input()
    if entrada == "Achou uma pessoa!":
        pontos_3 = pontos_3 + 1
        print(nome_3,"achou uma pessoa!")

#CIN   
print("Agora",nome_3,"procurará no",predio_3+".")
entrada = ""
while entrada != "Fim da busca nesse prédio.":
    entrada = input()
    if entrada == "Achou uma pessoa!":
        pontos_3 = pontos_3+ 1
        print(nome_3,"achou uma pessoa!")



vencedor = ""
 ##===== Decidir vencedor =====##
if pontos_1 == 0 and pontos_2 == 0 and pontos_3 == 0:
    print()
    print("Ninguém foi encontrado, nenhum dos buscadores ganhou a disputa.")
else:
    if pontos_1 > pontos_2 and pontos_2 > pontos_3:
        vencedor = nome_1
    elif pontos_2 > pontos_1 and pontos_2 > pontos_3:
        vencedor = nome_2
    else:
        vencedor = nome_3
    print()
    print(f"{vencedor} é o(a) melhor no esconde-esconde da UFPE!")
        



