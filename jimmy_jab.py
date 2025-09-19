# O Jimmy Jab é dividido em 3 provas: 
# - A Bocatona 
# - A Corrida Volumosa
# - O Grande Circuito Final
#
# A competição será baseada nos dois finalistas de cada prova.
#
# Ou seja, o Grande Circuito Final contará com os finalistas da Bocatona e da Corrida Volumosa.
#
# Ao todo, 4 detetives vão participar. No entanto, o Sargento Jeffords ou o Capitão Holt 
# podem estar infiltrados, o que pode fazer a competição ser cancelada.
#
# Portanto, a primeira parte do código deve garantir que a corrida só aconteça 
# se um dos 4 detetives não for o Capitão Holt nem o Sargento Jeffords

participante_1 = input()
participante_2 = input()
participante_3 = input()
participante_4 = input()

print("Bem-vindos ao Jimmy Jab!")

if (participante_1 == "Terry" or participante_1 == "Holt") or (participante_2 == "Terry" or participante_2 == "Holt") or (participante_3 == "Terry" or participante_3 == "Holt") or (participante_4 == "Terry" or participante_4 == "Holt"):  
    print("Jimmy Jab CANCELADO!")
else:
    print("Nosso primeiro evento é...")
    print("A Bocatona!")
    
    # Verifica se Scully está presente
    tem_scully = participante_1 == "Scully" or participante_2 == "Scully" or participante_3 == "Scully" or participante_4 == "Scully"
        
    if tem_scully:
        print("Scully leva a melhor, não tem como competir com ele.")
        perdedor_bocatona = input()
        vencedor_bocatona = "Scully"
        print(f"{vencedor_bocatona} levou a melhor na Bocatona!")
    else:
        vencedor_bocatona = input()
        perdedor_bocatona = input()
        print(f"{vencedor_bocatona} levou a melhor na Bocatona!")
        perdedor_bocatona = input()
        
    if participante_1 == perdedor_bocatona:
        perdedor_atual = perdedor_bocatona
    elif participante_2 == perdedor_bocatona:
        perdedor_atual = perdedor_bocatona
    elif participante_3 == perdedor_bocatona:
        perdedor_atual = perdedor_bocatona
    elif participante_4 == perdedor_bocatona:
        perdedor_atual = perdedor_bocatona
    

    print("O segundo evento é A corrida volumosa!")

    if participante_4 == perdedor_atual:
        tempo_participante_1 = int(input())
        tempo_participante_2 = int(input())
        tempo_participante_3 = int(input())
        if tempo_participante_1 < tempo_participante_2 and tempo_participante_1 < tempo_participante_3:
            vencedor = participante_1
            if tempo_participante_2 < tempo_participante_3:
                vencedor_2 = participante_2
            else:
                vencedor_2 = participante_3
            print(f"{vencedor} levou a melhor na Corrida Volumosa!")
            print(f"{vencedor_2} levou a melhor na Corrida Volumosa!")
        elif tempo_participante_2 < tempo_participante_1 and tempo_participante_2 < tempo_participante_3:
            vencedor = participante_2
            if tempo_participante_1 < tempo_participante_3:
                vencedor_2 = participante_1
            else:
                vencedor_2 = participante_3
            print(f"{vencedor} levou a melhor na Corrida Volumosa!")
            print(f"{vencedor_2} levou a melhor na Corrida Volumosa!")
        else:
            vencedor = participante_3
            if tempo_participante_1 < tempo_participante_2:
                vencedor_2 = participante_1
            else:
                vencedor_2 = participante_2
            print(f"{vencedor} levou a melhor na Corrida Volumosa!")
            print(f"{vencedor_2} levou a melhor na Corrida Volumosa!")
            
    elif participante_3 == perdedor_atual:
        tempo_participante_1 = int(input())
        tempo_participante_2 = int(input())
        tempo_participante_4 = int(input())
        if tempo_participante_1 < tempo_participante_2 and tempo_participante_1 < tempo_participante_4:
            vencedor = participante_1
            if tempo_participante_2 < tempo_participante_4:
                vencedor_2 = participante_2
            else:
                vencedor_2 = participante_4
            print(f"{vencedor} levou a melhor na Corrida Volumosa!")
            print(f"{vencedor_2} levou a melhor na Corrida Volumosa!")
        elif tempo_participante_2 < tempo_participante_1 and tempo_participante_2 < tempo_participante_4:
            vencedor = participante_2
            if tempo_participante_1 < tempo_participante_4:
                vencedor_2 = participante_1
            else:
                vencedor_2 = participante_4
            print(f"{vencedor} levou a melhor na Corrida Volumosa!")
            print(f"{vencedor_2} levou a melhor na Corrida Volumosa!")
        else:
            vencedor = participante_4
            if tempo_participante_1 < tempo_participante_2:
                vencedor_2 = participante_1
            else:
                vencedor_2 = participante_2
            print(f"{vencedor} levou a melhor na Corrida Volumosa!")
            print(f"{vencedor_2} levou a melhor na Corrida Volumosa!")

    elif participante_2 == perdedor_atual:
        tempo_participante_1 = int(input())
        tempo_participante_3 = int(input())
        tempo_participante_4 = int(input())
        if tempo_participante_1 < tempo_participante_3 and tempo_participante_1 < tempo_participante_4:
            vencedor = participante_1
            if tempo_participante_3 < tempo_participante_4:
                vencedor_2 = participante_3
            else:
                vencedor_2 = participante_4
            print(f"{vencedor} levou a melhor na Corrida Volumosa!")
            print(f"{vencedor_2} levou a melhor na Corrida Volumosa!")
        elif tempo_participante_3 < tempo_participante_1 and tempo_participante_3 < tempo_participante_4:
            vencedor = participante_3
            if tempo_participante_1 < tempo_participante_4:
                vencedor_2 = participante_1
            else:
                vencedor_2 = participante_4
            print(f"{vencedor} levou a melhor na Corrida Volumosa!")
            print(f"{vencedor_2} levou a melhor na Corrida Volumosa!")
        else:
            vencedor = participante_4
            if tempo_participante_1 < tempo_participante_3:
                vencedor_2 = participante_1
            else:
                vencedor_2 = participante_3
            print(f"{vencedor} levou a melhor na Corrida Volumosa!")
            print(f"{vencedor_2} levou a melhor na Corrida Volumosa!")
    
    elif participante_1 == perdedor_atual:
        tempo_participante_2 = int(input())
        tempo_participante_3 = int(input())
        tempo_participante_4 = int(input())
        if tempo_participante_2 < tempo_participante_3 and tempo_participante_2 < tempo_participante_4:
            vencedor = participante_2
            if tempo_participante_3 < tempo_participante_4:
                vencedor_2 = participante_3
            else:
                vencedor_2 = participante_4
            print(f"{vencedor} levou a melhor na Corrida Volumosa!")
            print(f"{vencedor_2} levou a melhor na Corrida Volumosa!")
        elif tempo_participante_3 < tempo_participante_2 and tempo_participante_3 < tempo_participante_4:
            vencedor = participante_3
            if tempo_participante_2 < tempo_participante_4:
                vencedor_2 = participante_2
            else:
                vencedor_2 = participante_4
            print(f"{vencedor} levou a melhor na Corrida Volumosa!")
            print(f"{vencedor_2} levou a melhor na Corrida Volumosa!")
        else:
            vencedor = participante_4
            if tempo_participante_2 < tempo_participante_3:
                vencedor_2 = participante_2
            else:
                vencedor_2 = participante_3
            print(f"{vencedor} levou a melhor na Corrida Volumosa!")
            print(f"{vencedor_2} levou a melhor na Corrida Volumosa!")
        
    if vencedor == "Amy" and vencedor_2 == "Jake":
        print("Jake ficou com o 2º lugar!")
        print("Amy VENCEU O JIMMY JABS!")
    elif vencedor == "Jake" and vencedor_2 == "Amy":
        print("Jake ficou com o 2º lugar!")
        print("Amy VENCEU O JIMMY JABS!")
    else:
        vencedor_final = input()
        if vencedor_final == vencedor:
            segundo_lugar = vencedor_2
        else:
            segundo_lugar = vencedor
    
    print(f"{segundo_lugar} ficou com o 2º lugar!")
    print(f"{vencedor_final} VENCEU O JIMMY JABS!")

