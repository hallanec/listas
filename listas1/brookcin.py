
#Requisitos para participação no campeonato
#1 - Localização: A localização dos casos trabalhados. As únicas válidas são Manhattan e Brooklyn.

#2 - Quantidade de casos: O detetive precisa ter completado pelo menos 20 casos.

#3 - Média diária: A quantidade de casos por dia precisa ser de pelo menos 0.5.

#4 - Assistências: Precisa ter ajudado pelo menos 5 outros detetives.

#5 - Operações de campo: O participante precisa ter participado de pelo menos 20 operações

#quantidade_casos = 2 
#numero_de_assistencias = peso 1.5
#operações_em_campo = peso 0.5

#Peralta pode ter participado (ou não) de uma OPERAÇÃO ESPECIAL, isso será determinado no input.
#Caso ele tenha participado, sua pontuação sofre um aumento percentual dependendo do tipo de operação especial. Veja:

#TIPO DE OPERAÇÃO ———- AUMENTO PERCENTUAL

#Infiltração ----------------- 50%
#Escuta ----------------- 30%
#Invasão ----------------- 20%
#Nenhuma das anteriores ------ 10%

## soma_ponderada =  soma_ponderada + (50/100 * soma_ponderada) 

#se ele não participa da operação especial, ele não ganha aumento percentual



casos = int(input())
dias = int(input())
media_casos = float(casos/dias)
assistencias_em_casos = int(input())
operacoes_em_campos = int(input())
operacao_especial = input()
if operacao_especial == "sim":
    tipo_operacao_especial = input()
localizacao = input()
soma_total = 0

if (localizacao == "Manhattan" or localizacao == "Brooklyn") and casos >= 20  and media_casos >= 0.5 and assistencias_em_casos >= 5 and operacoes_em_campos >= 20 :
    qtd_casos = casos * 2
    qtd_assist = 1.5 * assistencias_em_casos
    qtd_operacoes = 0.5 * operacoes_em_campos
    soma_total =  (qtd_casos + qtd_assist + qtd_operacoes)

    if operacao_especial == "sim": 
        if tipo_operacao_especial == "Infiltração":
            soma_total = soma_total + (soma_total* 0.5)
        elif tipo_operacao_especial == "Escuta":
            soma_total = soma_total + (soma_total * 0.3)
        elif tipo_operacao_especial == "Invasão":
            soma_total = soma_total + (soma_total * 0.2)
        elif tipo_operacao_especial != "Infiltração" and tipo_operacao_especial != "Escuta" and tipo_operacao_especial != "Invasão":
            soma_total = soma_total + (soma_total * 0.1)


if (localizacao == "Manhattan" or localizacao == "Brooklyn"):
    print("Pelo menos nos bairros corretos Jake está!")
    
    if casos >= 20:
        print("Detetive Peralta bateu o mínimo de casos, ele ainda está dentro da competição.")
        
        if media_casos >= 0.5:
            print("Parece que Jake é bem consistente na sua média diária de casos.")
            if assistencias_em_casos >= 5:
                print("Peralta ajudou bastante outros detetives, ele ainda está na competição!")
                if operacoes_em_campos >= 20:
                    print("Jake ainda sobrevive por sua participação em campo, será que ele vai levar pra casa o prêmio?")
                    if operacao_especial == "sim":
                        print("Minha nossa! Jake Peralta é realmente um detetive diferenciado.")
                    else:
                        print("Para que operação especial quando se tem números, não é?") 
                    if soma_total != 0:

                        if soma_total >= 70:
                            print("Jake é candidato forte ao prêmio. Será que Holt vai premiá-lo?") 
                        elif soma_total >= 40 and soma_total < 70:
                            print("Muito bem! Mas ainda é incerto se vai ser suficiente para ganhar o prêmio.")
                        elif soma_total < 40:
                            print("Muito difícil de Jake ganhar o prêmio.")                           
                else:
                    print("Peralta precisa sair mais da delegacia, está faltando ação em campo!")                       
            else:
                print("Desclassificado! Jake precisa ajudar mais os companheiros.") 
        else:
            print("A média diária de casos tá muito baixa, Peralta foi desclassificado.")

    else:
        print("Vishh, Jake já foi eliminado por não ter o mínimo de casos necessários.")
else:
    print("Os casos não são nas áreas designadas por Holt. Peralta está desclassificado!")











