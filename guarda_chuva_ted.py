#x1 (coordenada X de Ted)
#y1 (coordenada Y de Ted)

x1 = int(input())
y1 = int(input())

amigo = input()

#x2 (coordenada X do guarda-chuva)
#y2 (coordenada Y do guarda-chuva)
# Amigo (str)

x2 = int(input())
y2 = int (input())

#distancia_original = √( (x2 - x1)² + (y2 - y1)² )

## potencia em python é "**"", e raiz quadrada é multiplicar por 0.5, ou seja 1/2
distancia_original = ((x2 - x1)**2 + (y2 - y1)**2)**1/2 

#Se o amigo for "Barney": A jornada é imprevisível. Ele pode te levar mais longe para uma aventura lendária.

#distancia_final = distancia_original + 10

#Se o amigo for "Marshall": Ele sempre te ajuda a chegar ao destino.

#distancia_final = distancia_original - 5

#Se o amigo for "Lily": Ela sabe os melhores atalhos.

#distancia_final = distancia_original - 10

#Se o amigo for "Robin": Ela é a mais independente e pode acabar te levando a um caminho não planejado.

#distancia_final = distancia_original + 5

if amigo == "Barney":
    distancia_final = distancia_original + 10
else:
    if amigo == "Marshall":
        distancia_final == distancia_original -5
    else:
        if amigo == "Lily":
            distancia_final = distancia_original - 10
        else:
            if amigo == "Robin":
                distancia_final = distancia_original + 5 
            



