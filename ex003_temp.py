doces = int(input())
jogador_1 = input()
jogador_2 = input()

# Verificar se Arthur está presente
if jogador_1 != "Arthur" and jogador_2 != "Arthur":
    print("Epa!!! E cadê o dono dos doces??")
else:
    print("A batalha vai começar!")
    rodada = 1

    while doces > 0:
        vida_1 = 10
        vida_2 = 10

        # Mensagem da rodada
        if rodada == 1 and doces % 10 != 0:
            print(f"Pra aquecer, essa primeira vale menos, só {doces % 10} doces!")
        else:
            print(f"Batalha número {rodada}!")

        # Loop de turnos da rodada
        primeira_jogada = True
        while vida_1 > 0 and vida_2 > 0:
            jogada_1 = input()
            jogada_2 = input()

            if jogada_1 == jogada_2:
                print("Eita, jogaram a mesma coisa dessa vez.")
            else:
                # Papel vs Tesoura
                if jogada_1 == "papel" and jogada_2 == "tesoura":
                    vida_1 -= 3
                    vida_2 += 1
                elif jogada_1 == "tesoura" and jogada_2 == "papel":
                    vida_1 += 1
                    vida_2 -= 3
                # Pedra vs Papel
                elif jogada_1 == "pedra" and jogada_2 == "papel":
                    vida_1 -= 2
                    vida_2 += 2
                elif jogada_1 == "papel" and jogada_2 == "pedra":
                    vida_1 += 2
                    vida_2 -= 2
                # Pedra vs Tesoura
                elif jogada_1 == "pedra" and jogada_2 == "tesoura":
                    vida_2 -= 4
                elif jogada_1 == "tesoura" and jogada_2 == "pedra":
                    vida_1 -= 4

                # Garantir que a vida não seja negativa
                if vida_1 < 0:
                    vida_1 = 0
                if vida_2 < 0:
                    vida_2 = 0

                # Imprimir estado do turno após aplicar mudanças
                print(f"Esse turno terminou com {jogador_1} tendo {vida_1} de vida e {jogador_2} tendo {vida_2}!")

        # Determinar ganhador da rodada
        ganhador = jogador_1 if vida_2 == 0 else jogador_2
        print(f"A rodada {rodada} vai para {ganhador}, que garante seus doces!")

        # Próxima rodada
        rodada += 1
        doces -= 10