# EC 2025.2 - Lista 1
# Pastelada do Beiçola 🍩
#
# Um desafio na pastelaria do Beiçola busca o maior comilão de pastéis da vizinhança.
# Três competidores participam, informando seus nomes e quantos pastéis comeram.
#
# Entrada:
# - nome_competidor1 (str)
# - pasteis_competidor1 (int)
# - nome_competidor2 (str)
# - pasteis_competidor2 (int)
# - nome_competidor3 (str)
# - pasteis_competidor3 (int)
#
# Regras:
# - Se "Lineu" estiver entre os competidores, a competição é cancelada:
#   >> "Lineu comeu um pastel com gosto estranho e usou sua autoridade na vigilancia sanitaria para acabar com a competição, Beiçola tá desolado!"
#
# - Caso contrário, mostre o campeão:
#   >> "A(O) campeã(o) é {nome_Campeao}, com {pasteis_Campeao} pastéis consumidos!"
#
# - Se "Floriano" participou e não venceu:
#   >> "Anos comendo pastel e perdeu justo para {nome_Campeao}, lastimável, Sr. Flor!"
#
# - Se o campeão for "Agostinho":
#   - > 100 pastéis:
#     >> "Acho que o Agostinho deve ter escondido alguns pastéis na calça, pilantra!"
#   - Entre 51 e 99:
#     >> "Agostinho madrugou no taxi e veio cheio de fome para a competição!"




nome_competidor1 = input()
pasteis_competidor1 = int(input())
nome_competidor2 = input()
pasteis_competidor2 = int(input())
nome_competidor3 = input()
pasteis_competidor3 = int(input())

Floriano = str("Floriano")
Lineu = str("Lineu")
Agostinho = str("Agostinho")

quantidade_vencedor = 0
vencedor = 0

if (nome_competidor1 == Lineu) or (nome_competidor2 == Lineu) or (nome_competidor3 == Lineu):
    print("Lineu comeu um pastel com gosto estranho e usou sua autoridade na vigilancia sanitaria para acabar com a competição, Beiçola tá desolado!")
elif pasteis_competidor1 > pasteis_competidor2 and pasteis_competidor1 > pasteis_competidor3:
    vencedor = nome_competidor1
    quantidade_vencedor = pasteis_competidor1
elif pasteis_competidor2 > pasteis_competidor1 and pasteis_competidor2 > pasteis_competidor3:
    vencedor = nome_competidor2
    quantidade_vencedor = pasteis_competidor2
elif  pasteis_competidor3 > pasteis_competidor1 and pasteis_competidor3 > pasteis_competidor2:
    vencedor = nome_competidor3
    quantidade_vencedor = pasteis_competidor3

print(f"A(O) campeã(o) é {vencedor}, com {quantidade_vencedor} pastéis consumidos!")

if ((nome_competidor1 == Floriano) or (nome_competidor2 == Floriano) or (nome_competidor3 == Floriano)) and (vencedor != Floriano):
    print(f"Anos comendo pastel e perdeu justo para {vencedor}, lastimável, Sr. Flor!")

if vencedor == Agostinho and quantidade_vencedor > 100:
    print("Acho que o Agostinho deve ter escondido alguns pastéis na calça, pilantra!")
elif vencedor == Agostinho and quantidade_vencedor > 50 and quantidade_vencedor < 100:
    print("Agostinho madrugou no taxi e veio cheio de fome para a competição!")




