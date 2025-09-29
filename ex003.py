doces = int(input())
jogador_1 = input()
jogador_2 = input()

if jogador_1 == "Arthur" or jogador_2 == "Arthur":
    print("A batalha vai começar!")
    jogo_valido = True
else:
    print("Epa!!! E cadê o dono dos doces??")
    jogo_valido = False

rodada = 1 

while doces > 0 and jogo_valido:
    vida_jogador_1 = 10
    vida_jogador_2 = 10
    
    if rodada == 1:
        resto_doces = doces % 10
        if resto_doces != 0:
            print("Pra aquecer, essa primeira vale menos, só ", resto_doces, " doces!")
        else:
            print("Batalha número ", rodada, "!")   
    else:
        print("Batalha número ", rodada, "!")
    
    while vida_jogador_1 > 0 and vida_jogador_2 >0:
        jogada_1 = input()
        jogada_2 = input()
        if jogada_1 == jogada_2:
            print("Eita, jogaram a mesma coisa dessa vez.")
            
        else:
            if jogada_1 == jogada_2:
                print("Eita, jogaram a mesma coisa dessa vez.")
            elif jogada_1 == "papel" and jogada_2 == "tesoura":
                vida_jogador_1 -= 3
                vida_jogador_2 += 1
            elif jogada_1 == "tesoura" and jogada_2 == "papel":
                vida_jogador_1 += 1
                vida_jogador_2 -= 3
            elif jogada_1 == "pedra" and jogada_2 == "papel":
                vida_jogador_1 -= 2
                vida_jogador_2 += 2
            elif jogada_1 == "papel" and jogada_2 == "pedra":
                vida_jogador_1 += 2
                vida_jogador_2 -= 2
            elif jogada_1 == "pedra" and jogada_2 == "tesoura":
                vida_jogador_2 -= 4
            elif jogada_1 == "tesoura" and jogada_2 == "pedra":
                vida_jogador_1 -= 4


             
              
        if vida_jogador_1 < 0:
            vida_jogador_1 = 0
        else:
            if vida_jogador_2 < 0:
                vida_jogador_2 = 0
        
        print("Esse turno terminou com ", jogador_1, " tendo ", vida_jogador_1, " de vida e ", jogador_2, " tendo ", vida_jogador_2, "!")

    if vida_jogador_1 <= 0:
        ganhador_rodada = jogador_2
    else:
        ganhador_rodada = jogador_1
        
    
    
    print("A rodada ", rodada, " vai para ", ganhador_rodada, ", que garante seus doces!")
    rodada = rodada +1
    doces = doces - 10