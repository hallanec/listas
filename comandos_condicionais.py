# Lista 1 - Comandos Condicionais
# E.C 2025.-2
#
# Problem Statement
#
# Durante uma noite comum no apartamento 4A, Sheldon, Leonard, Raj e Howard estavam discutindo
# quem tinha feito a maior contribuição científica da semana. Como ninguém confiava em ninguém,
# Sheldon decidiu elaborar um sistema de pontuação altamente objetivo (segundo ele).
#
# Seu papel é programar esse sistema para descobrir quem é o cientista da semana.
#
# Boa sorte, Bazinga!!
#
# Regras
#
# A pontuação final de cada participante é dada por:
# pontuação = artigos * 2 + experimentos * 3
#
# O jogador com a maior pontuação é declarado o cientista da semana.
#
# Caso haja empate entre dois ou mais:
# - Se Sheldon estiver entre os empatados, ele automaticamente se declara vencedor.
# - Caso Sheldon não esteja entre os empatados, o vencedor será aquele cujo nome aparecer primeiro
#   na ordem: Leonard → Raj → Howard.
#
# Input
#
# O programa receberá os seguintes valores, nesta ordem:
# - Número de artigos lidos por Sheldon (int).
# - Número de artigos lidos por Leonard (int).
# - Número de artigos lidos por Raj (int).
# - Número de artigos lidos por Howard (int).
# - Número de experimentos realizados por Sheldon (int).
# - Número de experimentos realizados por Leonard (int).
# - Número de experimentos realizados por Raj (int).
# - Número de experimentos realizados por Howard (int).
#
# Output
#
# O programa deve imprimir:
#
# Pontuação final:
# Sheldon: X
# Leonard: Y
# Raj: Z
# Howard: W
#
# Em seguida, pule uma linha e imprima a mensagem com o vencedor:
# O cientista da semana é: NOME
#
# Se o vencedor for o Sheldon você deve imprimir:
# Não é atoa que ele ganhou o prêmio Nobel
#
# Se o vencedor for o Leonard você deve imprimir:
# A vitória dele prova que aguentar o Sheldon já é um experimento científico por si só.
#
# Se o vencedor for o Raj você deve imprimir:
# Ele comemora... mas ainda precisa da ajuda do cachorro para falar com mulheres.
#
# Se o vencedor for o Howard você deve imprimir:
# Um pequeno passo para a ciência, um grande salto para alguém com mestrado.

numero_artigos_lidos_por_sheldon = int(input())
numero_de_artigos_lidos_por_leonard = int(input())
numero_de_artigos_lidos_por_raj = int(input())
numero_de_artigos_lidos_por_howard = int(input())
numero_de_experimentos_realizados_por_sheldon = int(input())
numero_de_experimentos_realizados_por_leonard = int(input())
numero_de_experimentos_realizados_por_raj = int(input())
numero_de_experimentos_realizados_por_howard = int(input())


# pontuação = artigos * 2 + experimentos * 3

pont_sheldon = (numero_artigos_lidos_por_sheldon*2) + (numero_de_experimentos_realizados_por_sheldon*3)
pont_leonard = (numero_de_artigos_lidos_por_leonard*2) + (numero_de_experimentos_realizados_por_leonard*3)
pont_raj = (numero_de_artigos_lidos_por_raj*2) + (numero_de_experimentos_realizados_por_raj*3)
pont_howard = (numero_de_artigos_lidos_por_howard*2) + (numero_de_experimentos_realizados_por_howard*3)


# Interpolação de variáveis é o nome dado ao processo de inserir o valor de uma variável dentro de uma string automaticamente.
#ex:nome = "Sheldon"
#print("O nome é " + nome)
#Com interpolação, você pode fazer:
#print(f"O nome é {nome}")

print(f"""Pontuação final:
Sheldon: {pont_sheldon}
Leonard: {pont_leonard}
Raj: {pont_raj}
Howard: {pont_howard}
""")

if pont_sheldon == pont_leonard == pont_raj == pont_howard:
    print("O cientista da semana é: Sheldon")
    print("Não é atoa que ele ganhou o prêmio Nobel")
elif pont_leonard > pont_raj and pont_leonard> pont_howard and pont_leonard > pont_sheldon:      
    print("O cientista da semana é: Leonard")
    print("A vitória dele prova que aguentar o Sheldon já é um experimento científico por si só.")
elif pont_raj > pont_sheldon and pont_raj > pont_leonard and pont_raj > pont_howard:
    print("O cientista da semana é: Raj")
    print("Ele comemora... mas ainda precisa da ajuda do cachorro para falar com mulheres.")
elif pont_howard > pont_leonard and pont_howard > pont_sheldon and pont_howard > pont_raj:
    print("O cientista da semana é: Howard")
    print("Um pequeno passo para a ciência, um grande salto para alguém com mestrado.")
elif pont_sheldon > pont_raj and pont_sheldon > pont_leonard and pont_sheldon > pont_howard:
    print("O cientista da semana é: Sheldon")
    print("Não é atoa que ele ganhou o prêmio Nobel")
elif pont_sheldon < pont_raj and pont_sheldon < pont_leonard and pont_sheldon < pont_howard and pont_leonard == pont_raj == pont_howard:
    print("O cientista da semana é: Leonard" )
    print("A vitória dele prova que aguentar o Sheldon já é um experimento científico por si só.")
elif pont_sheldon < pont_raj and pont_sheldon < pont_leonard and pont_sheldon < pont_howard and pont_leonard < pont_raj and  pont_leonard < pont_howard and pont_raj == pont_howard:
    print("O cientista da semana é: Raj")
    print("Ele comemora... mas ainda precisa da ajuda do cachorro para falar com mulheres.")
elif pont_sheldon < pont_raj and pont_sheldon < pont_leonard and pont_sheldon < pont_howard and pont_leonard > pont_raj and  pont_leonard == pont_howard and pont_raj < pont_howard:
    print("O cientista da semana é: Leonard")
    print("A vitória dele prova que aguentar o Sheldon já é um experimento científico por si só.")
elif pont_sheldon == pont_leonard and pont_sheldon > pont_raj and pont_sheldon > pont_howard:
    print("O cientista da semana é: Sheldon")
    print("Não é atoa que ele ganhou o prêmio Nobel")
elif pont_sheldon == pont_raj and pont_sheldon > pont_leonard and pont_sheldon > pont_howard:
    print("O cientista da semana é: Sheldon")
    print("Não é atoa que ele ganhou o prêmio Nobel")
elif pont_sheldon == pont_howard and pont_sheldon > pont_leonard and pont_sheldon > pont_raj:
    print("O cientista da semana é: Sheldon")
    print("Não é atoa que ele ganhou o prêmio Nobel")
    



    
    