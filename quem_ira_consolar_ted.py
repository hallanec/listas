# Input inicial
quantidade_pessoas = int(input())

# Outputs iniciais
print("Ted se iludiu de novo. Esse é o momento que ele mais precisa dos amigos dele…")
print("Quantos dos amigos dele conseguirão ajudar dessa vez?")

# Inicializa todas as variáveis
nome1 = ""
nome2 = ""
nome3 = ""
nome4 = ""
total_cervejas = 0
quantidade_media_cervejas = 0

# Caso Ted vá sozinho
if quantidade_pessoas == 0:
    quantidade_media_cervejas = int(input())
    total_cervejas = quantidade_media_cervejas
    print()
    print("Relatório da situação de Ted:")
    print("Ted foi para o MacLaren’s… Olhe em volta, Ted, você está sozinho.")
    print(f"- Quantidade de cervejas bebidas por Ted: {total_cervejas} cervejas.")
else:
    print("Hora da lista dos amigos da vez!")

    # Entrada dos nomes conforme a quantidade de pessoas
    if quantidade_pessoas >= 1:
        nome1 = input()
    if quantidade_pessoas >= 2:
        nome2 = input()
    if quantidade_pessoas >= 3:
        nome3 = input()
    if quantidade_pessoas == 4:
        nome4 = input()

    # Mensagens individuais
    if quantidade_pessoas >= 1:
        if nome1 == "Barney":
            print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
        elif nome1 == "Robin":
            print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
        elif nome1 == "Marshall":
            print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
        elif nome1 == "Lily":
            print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
        else:
            print(f"{nome1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")

    if quantidade_pessoas >= 2:
        if nome2 == "Barney":
            print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
        elif nome2 == "Robin":
            print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
        elif nome2 == "Marshall":
            print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
        elif nome2 == "Lily":
            print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
        else:
            print(f"{nome2} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")

    if quantidade_pessoas >= 3:
        if nome3 == "Barney":
            print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
        elif nome3 == "Robin":
            print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
        elif nome3 == "Marshall":
            print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
        elif nome3 == "Lily":
            print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
        else:
            print(f"{nome3} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")

    if quantidade_pessoas == 4:
        if nome4 == "Barney":
            print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
        elif nome4 == "Robin":
            print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
        elif nome4 == "Marshall":
            print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
        elif nome4 == "Lily":
            print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
        else:
            print(f"{nome4} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")

    # Mensagens especiais de acordo com nomes
    if quantidade_pessoas == 2:
        if (nome1 == "Marshall" and nome2 == "Lily") or (nome1 == "Lily" and nome2 == "Marshall"):
            print("Nada melhor que um casal para dar conselhos de relacionamento.")
        elif (nome1 == "Barney" and nome2 == "Marshall") or (nome1 == "Marshall" and nome2 == "Barney"):
            print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.")
    if quantidade_pessoas == 4:
        if ((nome1 == "Barney" or nome2 == "Barney" or nome3 == "Barney" or nome4 == "Barney") and
            (nome1 == "Robin" or nome2 == "Robin" or nome3 == "Robin" or nome4 == "Robin") and
            (nome1 == "Marshall" or nome2 == "Marshall" or nome3 == "Marshall" or nome4 == "Marshall") and
            (nome1 == "Lily" or nome2 == "Lily" or nome3 == "Lily" or nome4 == "Lily")):
            print("O quinteto estará reunido nessa jornada! É o momento perfeito pra brincar de “Você conhece o Ted?”.")
        

    # Entrada do lugar
    lugar = input()

    # Mensagens especiais de acordo com o lugar
    if lugar == "MacLaren’s Pub":
        quantidade_media_cervejas = int(input())
        total_cervejas = quantidade_media_cervejas * (quantidade_pessoas +1)
        if ((quantidade_pessoas >= 1 and (nome1 == "Barney" or nome1 == "Robin" or nome1 == "Marshall" or nome1 == "Lily")) or
            (quantidade_pessoas >= 2 and (nome2 == "Barney" or nome2 == "Robin" or nome2 == "Marshall" or nome2 == "Lily")) or
            (quantidade_pessoas >= 3 and (nome3 == "Barney" or nome3 == "Robin" or nome3 == "Marshall" or nome3 == "Lily")) or
            (quantidade_pessoas == 4 and (nome4 == "Barney" or nome4 == "Robin" or nome4 == "Marshall" or nome4 == "Lily"))):
            print("Não tem erro, né? Estar no MacLaren’s é como estar em casa.")
        else:
            print("Um lugar habitual, mas com uma galera diferente. Será estranho, mas Ted vai.")
    elif lugar == "Arena de Laser Tag":
        if ((quantidade_pessoas >= 1 and nome1 == "Barney") or
            (quantidade_pessoas >= 2 and nome2 == "Barney") or
            (quantidade_pessoas >= 3 and nome3 == "Barney") or
            (quantidade_pessoas == 4 and nome4 == "Barney")):
            print("Com certeza a Arena de Laser Tag foi escolhida por influência de Barney. Se arrume Ted, é hora de botar um terno, tomar um whisky e partir pra diversão.")
    elif lugar == "Carmichael’s":
        if (quantidade_pessoas == 1 and nome1 == "Robin") or \
   (quantidade_pessoas == 2 and (
        (nome1 == "Robin" and nome2 != "Barney" and nome2 != "Marshall" and nome2 != "Lily") or
        (nome2 == "Robin" and nome1 != "Barney" and nome1 != "Marshall" and nome1 != "Lily")
    )) or \
   (quantidade_pessoas == 3 and (
        (nome1 == "Robin" and nome2 != "Barney" and nome2 != "Marshall" and nome2 != "Lily" and nome3 != "Barney" and nome3 != "Marshall" and nome3 != "Lily") or
        (nome2 == "Robin" and nome1 != "Barney" and nome1 != "Marshall" and nome1 != "Lily" and nome3 != "Barney" and nome3 != "Marshall" and nome3 != "Lily") or
        (nome3 == "Robin" and nome1 != "Barney" and nome1 != "Marshall" and nome1 != "Lily" and nome2 != "Barney" and nome2 != "Marshall" and nome2 != "Lily")
    )) or \
   (quantidade_pessoas == 4 and (
        (nome1 == "Robin" or nome2 == "Robin" or nome3 == "Robin" or nome4 == "Robin")
    )):
            print("Acho que Ted e Robin vão sair em um date… Tomara que Ted não roube aquela trompa azul da parede de novo.")

    # Frase final de acordo com a quantidade de pessoas
    if quantidade_pessoas == 1:
        frase = "Saideira de um pra um. Nada melhor do que uma pessoa pra ouvir seus problemas."
    elif quantidade_pessoas == 2:
        frase = "Duas pessoas se compadeceram com a situação do pobre Ted."
    elif quantidade_pessoas == 3:
        frase = "Três pessoas! Ted conseguiu se divertir bastante."
    elif quantidade_pessoas == 4:
        if ((nome1 == "Barney" or nome2 == "Barney" or nome3 == "Barney" or nome4 == "Barney") and
            (nome1 == "Robin" or nome2 == "Robin" or nome3 == "Robin" or nome4 == "Robin") and
            (nome1 == "Marshall" or nome2 == "Marshall" or nome3 == "Marshall" or nome4 == "Marshall") and
            (nome1 == "Lily" or nome2 == "Lily" or nome3 == "Lily" or nome4 == "Lily")):
            frase = "O quinteto junto consegue resolver qualquer problema!"
        else:
            frase = "Saiu um quinteto um pouco diferente do que a gente tá acostumado, mas no fim conseguiram deixar Ted alegre."
        
    # Relatório final

if quantidade_pessoas >= 1:
  print()
  print("Relatório da situação de Ted:")
  if quantidade_pessoas == 1:
    print(f"- Ted foi consolado por: {nome1}.")
  elif quantidade_pessoas == 2:
      print(f"- Ted foi consolado por: {nome1} e {nome2}.")
  elif quantidade_pessoas == 3:
      print(f"- Ted foi consolado por: {nome1}, {nome2} e {nome3}.")
  elif quantidade_pessoas == 4:
      print(f"- Ted foi consolado por: {nome1}, {nome2}, {nome3} e {nome4}.")
  print(f"- O local de afogar as mágoas foi: {lugar}.")
  print(f"- {frase}")
  if total_cervejas > 0:
      print(f"- Quantidade de cervejas bebidas pelo grupo: {total_cervejas} cervejas.")
  print("Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?")


  

