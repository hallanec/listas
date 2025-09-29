# Quantidade de participantes
N = int(input())
# Primeiro participante (para pegar a palavra de referência)
nome_participante_1= input()
palavra_referencia = input()

print("Vai começar a brincadeira! Será que a palavra vai ficar igual até o fim?")

todas_diferentes = True
contador_diferentes = 0
mensagem_especial_printada = False
palavra_anterior = palavra_referencia


# Agora loop para os demais participantes (do 2 ao N)
for i in range(2, N+1):
    
    nome_participante_2 = input()
    palavra_falada = input()
    
    if palavra_falada != palavra_anterior:
        print(f"Parece que {nome_participante_2} não conseguiu ouvir muito bem e acabou passando pra frente uma palavra diferente da que escutou…")
        contador_diferentes += 1
        
        
        if contador_diferentes == 1:
            unico_jogador = nome_participante_2
            unica_palavra = palavra_falada
        elif contador_diferentes == 2:
            nome_jogador_2 = nome_participante_2
 
        if contador_diferentes == 5 and not mensagem_especial_printada:
            print(f"Caramba, que confusão! A palavra {palavra_referencia} já tá toda embaralhada e virou {palavra_falada}!")
            mensagem_especial_printada = True  # 
    
    palavra_anterior = palavra_falada
  
palavra_final = palavra_anterior
      
if contador_diferentes == 0:
    print(f"Impressionante, todos os jogadores ouviram e falaram perfeitamente a palavra {palavra_final}! Talvez os telefones modernos comecem a perder espaço pra moda antiga.")
elif palavra_final == palavra_referencia:
    print(f"Parece que ocorreram {contador_diferentes} trocas durante o processo, mas mesmo com essa pequena confusão, a palavra {palavra_final} conseguiu chegar no fim do telefone sem fio.")

if palavra_final != palavra_referencia:       
    if contador_diferentes == 1:
        print(f"Poxa, foi por pouco, só quem errou foi {unico_jogador} que disse {unica_palavra} ao invés de {palavra_referencia}…")
    elif contador_diferentes == 2:
        print(f"Se não fosse pelos erros de {unico_jogador} e {nome_jogador_2}, a palavra {palavra_referencia} poderia ter chegado até o fim, talvez eles devessem tentar de novo.")

    else:
        if contador_diferentes> 2:
            print(f"É, parece que os alunos se confundiram bastante durante a brincadeira e a palavra {palavra_final} acabou virando {palavra_falada}. No total, ocorreram {contador_diferentes} trocas.")



    

        
    

    




    


