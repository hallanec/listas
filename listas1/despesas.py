item_comprado = input().lower()
valor_do_item = float(input())
responsavel_pela_compra = input().capitalize()
tipo_evento = input().lower()

if valor_do_item > 100 and responsavel_pela_compra != "Angela":
    print("Compra Reprovada!")
    print("Gasto excessivo e irresponsável! Onde está a disciplina fiscal?!")
elif valor_do_item > 100 and responsavel_pela_compra == "Angela":
    print("Compra Aprovada!")
    print("Apenas eu tenho discernimento para gastos desta magnitude.")
elif valor_do_item > 0 and valor_do_item <= 100 and responsavel_pela_compra == "Angela":
    print("Compra Aprovada!")
    print("Compra feita por mim, obviamente dentro dos padrões de excelência.")
elif responsavel_pela_compra == "Michael" and (item_comprado == "mágica" or item_comprado == "fantasia"):
    print("Compra Reprovada!")
    print("O Comitê não financia frivolidades e palhaçadas, Michael.")
elif responsavel_pela_compra == "Michael" and valor_do_item > 60 and tipo_evento == "natal":
    print("Compra Aprovada com ressalvas!")
    print("O espírito natalino de Michael é... excessivo. A nota será conferida.")
elif responsavel_pela_compra == "Michael" and valor_do_item > 60 and tipo_evento == "aniversário":
    print("Compra Aprovada com ressalvas!")
    print("Michael nunca gasta tanto nos aniversários dos funcionários, deve ser o dele!")
elif responsavel_pela_compra == "Michael" and valor_do_item <= 60 :
    print("Compra Aprovada!")
    print("Uma compra surpreendentemente sensata vinda do Michael. Suspeito.")
elif tipo_evento == "halloween" and item_comprado == "abóbora" and valor_do_item <= 30:
    print("Compra Aprovada!")
    print("Uma abóbora de tamanho e custo razoáveis. Eficiente.")
elif tipo_evento == "halloween" and item_comprado == "abóbora" and valor_do_item > 30:
    print("Compra Aprovada com ressalvas!")
    print("Por que uma abóbora precisa ser tão cara? Extravagância.")
elif tipo_evento == "halloween" and valor_do_item <= 100:
    print("Compra Aprovada com ressalvas!")
    print("Decoração de Halloween... Tenho certeza que Phyllis exagerou de novo.")
elif tipo_evento == "aniversário" and item_comprado == "bolo" and valor_do_item <= 40:
    print("Compra Aprovada!")
    print("Um bolo modesto para celebrar mais um ano de produtividade, parabéns!")
elif tipo_evento == "aniversário" and item_comprado == "sorvete de menta com chocolate":
    print("Compra Reprovada!")
    print("Este sabor de sorvete é uma abominação e não entrará em meu evento.")
elif tipo_evento == "aniversário":
    print("Compra Aprovada!")
    print("Itens de aniversário devem ser práticos, não uma distração do trabalho.")
elif tipo_evento != "halloween" and tipo_evento != "aniversário" and responsavel_pela_compra != "Michael" and responsavel_pela_compra != "Angela" and valor_do_item > 50:
    print("Compra Aprovada com ressalvas!")
    print("Está dentro do orçamento, mas não quer dizer que não vou verificar!")  
else: 
    print("Compra Aprovada!")
    print("Esta compra não viola nenhum regulamento... por enquanto.")