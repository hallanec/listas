#x1 (coordenada X de Ted)
#y1 (coordenada Y de Ted)

x1 = int(input())
y1 = int(input())


#x2 (coordenada X do guarda-chuva)
#y2 (coordenada Y do guarda-chuva)
# Amigo (str)

x2 = int(input())
y2 = int(input())

amigo = input()

#distancia_original = √( (x2 - x1)² + (y2 - y1)² )

## potencia em python é "**"", e raiz quadrada é multiplicar por 0.5, ou seja 1/2
distancia_original = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

#Se o amigo for "Barney": A jornada é imprevisível. Ele pode te levar mais longe para uma aventura lendária.

#distancia_final = distancia_original + 10

#Se o amigo for "Marshall": Ele sempre te ajuda a chegar ao destino.

#distancia_final = distancia_original - 5

#Se o amigo for "Lily": Ela sabe os melhores atalhos.

#distancia_final = distancia_original - 10

#Se o amigo for "Robin": Ela é a mais independente e pode acabar te levando a um caminho não planejado.

#distancia_final = distancia_original + 5

distancia_final = 0

if amigo == "Barney":
    distancia_final = distancia_original + 10
else:
    if amigo == "Marshall":
        distancia_final = distancia_original -5
    else:
        if amigo == "Lily":
            distancia_final = distancia_original - 10
        else:
            if amigo == "Robin":
                distancia_final = distancia_original + 5 
            else:
                distancia_final = distancia_original
            

# Se você quer saber se um número é do tipo float (tem parte decimal):
# Se você quiser arredondar para o inteiro mais próximo, use round():
distancia_final = round(distancia_final)

print(f"Pelos meus cálculos a distância final encontrada foi {distancia_final}!")

if distancia_final <= 50 and amigo == "Barney":
    print("Nossa, eu sou incrível! Vimos o guarda-chuva em 5 minutos. Tão lendário que eu poderia até ter pego ele pra mim! Desafio aceito!")
elif distancia_final <= 50 and amigo == "Marshall":
    print("Obrigado pela ajuda, Marsh! Tão bom saber que a gente pode contar com os amigos pra achar a nossa cara-metade. Encontramos o guarda-chuva!")
elif distancia_final <= 50 and amigo == "Lily":
    print("Ah! Não te falei? Peguei um atalho! Lilypad sabe das coisas. O guarda-chuva está aqui, e nem nos cansamos muito!")
elif distancia_final <= 50 and amigo == "Robin":
    print("Bem... acho que isso realmente aconteceu. Nem foi tão difícil assim. O guarda-chuva está bem aqui, Ted. Onde está o mistério?")
elif distancia_final > 50 and amigo == "Barney":
    print("Esse não era o caminho para o guarda-chuva, mas com certeza é o caminho para uma noite lendária! Challenge accepted, vista seu terno!")
elif distancia_final > 50 and amigo == "Marshall":
    print("Tudo bem, cara. O destino é paciente. O importante é que estamos juntos nessa. Vamos tentar de novo amanhã.")
elif distancia_final > 50 and amigo == "Lily":
    print("Isso não faz sentido! Meu atalho deveria ter funcionado! Que saco! Fiquei com fome de tanta caminhada.")
elif distancia_final > 50 and amigo == "Robin":
    print("Sério, Ted? Um guarda-chuva? O destino é um conceito abstrato.")


print("Faz o L")
            