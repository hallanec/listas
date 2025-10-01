bolinhas_andre = int(input())
bolinhas_bruno = int(input())
bolinhas_clara = int(input())

#fila = 1, 2 , 3 
#fila = andre, bruno, clara

resultado_rodada = input()

jogador_atual = 0
segundo_jogador = 0
terceiro_jogador = 0

acertos_andre = 0 
acertos_bruno = 0
acertos_clara = 0

erros_andre = 0
erros_bruno = 0 
erros_clara = 0

jogador_atual = bolinhas_andre

perdedor_1 = 1 
perdedor_2 = 1

while perdedor_1 != 0 and perdedor_2 != 0:
      
    if jogador_atual == bolinhas_andre:
        segundo_jogador = bolinhas_bruno
        terceiro_jogador = bolinhas_clara
    elif jogador_atual == bolinhas_bruno:
        segundo_jogador = bolinhas_clara
        terceiro_jogador = bolinhas_andre
    elif jogador_atual == bolinhas_clara:
        segundo_jogador = bolinhas_andre
        terceiro_jogador = bolinhas_bruno

    while resultado_rodada == "ACERTOU" :
        if jogador_atual == bolinhas_andre:
            bolinhas_andre = bolinhas_andre + 2 
            while segundo_jogador > 0:
                segundo_jogador = segundo_jogador - 1 
            while terceiro_jogador > 0:
                terceiro_jogador = terceiro_jogador - 1
            if segundo_jogador == 0:
                perdedor_1 = 1
            
            if terceiro_jogador == 0:
                perdedor_1 = 1

        elif jogador_atual == bolinhas_bruno:
            bolinhas_bruno = bolinhas_bruno + 2 
            while segundo_jogador > 0:
                segundo_jogador = segundo_jogador - 1 
            while terceiro_jogador > 0:
                terceiro_jogador = terceiro_jogador - 1
            if segundo_jogador == 0:
                perdedor_1 = 1
            
            if terceiro_jogador == 0:
                perdedor_1 = 1
                
        elif jogador_atual == bolinhas_bruno:
            bolinhas_andre = bolinhas_bruno + 2 
            while segundo_jogador > 0:
                segundo_jogador = segundo_jogador - 1 
            while terceiro_jogador > 0:
                terceiro_jogador = terceiro_jogador - 1
            if segundo_jogador == 0:
                perdedor_1 = 1
            
            if terceiro_jogador == 0:
                perdedor_1 = 1
        

        else:
            if jogador_atual == bolinhas_andre:
                erros_andre = erros_andre + 1 
            elif jogador_atual == bolinhas_bruno:   
                erros_bruno = erros_bruno + 1 
            elif jogador_atual == bolinhas_clara:
                erros_clara = erros_clara +1
            
            if jogador_atual == bolinhas_andre:
                while erros_andre < 3:
                    if resultado_rodada == "ERROU":
                        bolinhas_andre = terceiro_jogador
            elif jogador_atual == bolinhas_bruno:
                while erros_bruno < 3:
                    if resultado_rodada == "ERROU":
                        bolinhas_bruno = terceiro_jogador
            elif jogador_atual == bolinhas_clara:
                while erros_bruno < 3:
                    if resultado_rodada == "ERROU":
                        bolinhas_clara = terceiro_jogador
            

            if erros_andre == 3:
                perdedor_2 = 0
                saiu_antes_acabar = "andre"
            elif erros_bruno == 3:
                perdedor_2 = 0
                saiu_antes_acabar = "bruno"
            elif erros_clara == 3:
                perdedor_2 = 0
                saiu_antes_acabar = "clara"




            


    

             
                


