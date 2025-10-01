bolinhas_andre = int(input())
bolinhas_bruno = int(input())
bolinhas_clara = int(input())

#fila = 1, 2 , 3 
#fila = andre, bruno, clara


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

perdedor_1 = True
perdedor_2 = True

while perdedor_1 != False and perdedor_2 != False:
     
    resultado_rodada = input()

    if jogador_atual == bolinhas_andre:
        segundo_jogador = bolinhas_bruno
        terceiro_jogador = bolinhas_clara
    elif jogador_atual == bolinhas_bruno:
        segundo_jogador = bolinhas_clara
        terceiro_jogador = bolinhas_andre
    elif jogador_atual == bolinhas_clara:
        segundo_jogador = bolinhas_andre
        terceiro_jogador = bolinhas_bruno
 
    if resultado_rodada == "acertou" :
        if jogador_atual == bolinhas_andre:
            
            bolinhas_andre = bolinhas_andre + 2 
            acertos_andre = bolinhas_andre + 1
            
            if segundo_jogador > 0:
                segundo_jogador = segundo_jogador - 1 
            elif terceiro_jogador > 0:
                terceiro_jogador = terceiro_jogador - 1
            
            if segundo_jogador == 0:
                perdedor_1 = False
            
            if terceiro_jogador == 0:
                perdedor_1 = False
            
            if bolinhas_andre == jogador_atual:
                bolinhas_bruno = jogador_atual
        elif jogador_atual == bolinhas_bruno:
            
            bolinhas_bruno = bolinhas_bruno + 2 
            acertos_bruno = bolinhas_bruno + 1 

            if segundo_jogador > 0:
                segundo_jogador = segundo_jogador - 1 
            elif terceiro_jogador > 0:
                terceiro_jogador = terceiro_jogador - 1
            
            
            if segundo_jogador == 0:
                perdedor_1 = False
            
            if terceiro_jogador == 0:
                perdedor_1 = False
            
            if bolinhas_bruno == jogador_atual:
                bolinhas_clara = jogador_atual
        elif jogador_atual == bolinhas_bruno:
           
            bolinhas_clara = bolinhas_clara + 2 
            acertos_clara = acertos_clara + 1
            
            if segundo_jogador > 0:
                segundo_jogador = segundo_jogador - 1 
            elif terceiro_jogador > 0:
                terceiro_jogador = terceiro_jogador - 1
            
            if segundo_jogador == 0:
                perdedor_1 = False
            
            if terceiro_jogador == 0:
                perdedor_1 = False
            
            if bolinhas_clara == jogador_atual:
                bolinhas_andre = jogador_atual
            
        else:
            if jogador_atual == bolinhas_andre:
                erros_andre = erros_andre + 1 
            elif jogador_atual == bolinhas_bruno:   
                erros_bruno = erros_bruno + 1 
            elif jogador_atual == bolinhas_clara:
                erros_clara = erros_clara +1
            
            if jogador_atual == bolinhas_andre:
                if erros_andre < 3:
                    if resultado_rodada == "errou":
                        bolinhas_bruno = jogador_atual
                        
            elif jogador_atual == bolinhas_bruno:
                if erros_bruno < 3:
                    if resultado_rodada == "errou":
                        bolinhas_clara = jogador_atual
            elif jogador_atual == bolinhas_clara:
                    if erros_bruno < 3:
                        if resultado_rodada == "errou":
                            bolinhas_andre = jogador_atual
            

            if erros_andre == 3:
                perdedor_2 = False
                saiu_antes_acabar = "andre"
            elif erros_bruno == 3:
                perdedor_2 = False
                saiu_antes_acabar = "bruno"
            elif erros_clara == 3:
                perdedor_2 = False
                saiu_antes_acabar = "clara"
                
    if jogador_atual > segundo_jogador and segundo_jogador < terceiro_jogador:
        vencedor = jogador_atual 
        if jogador_atual == bolinhas_andre:
            vencedor = "andre"
        elif jogador_atual == bolinhas_bruno:
            vencedor = "bruno"
        else:
            vencedor = "clara"
    elif jogador_atual < segundo_jogador and segundo_jogador > terceiro_jogador:
        vencedor = segundo_jogador
        if segundo_jogador == bolinhas_andre:
            vencedor = "andre"
        elif segundo_jogador == bolinhas_bruno:
            vencedor = "bruno"
        else:
            vencedor = "clara" 
    else:
            if terceiro_jogador == bolinhas_andre:
                vencedor = "andre"
            elif terceiro_jogador == bolinhas_bruno:
                vencedor = "bruno"
            else:
                vencedor = "clara" 
                
    
      

print(acertos_andre)
print(acertos_bruno)
print (vencedor)
             
                


