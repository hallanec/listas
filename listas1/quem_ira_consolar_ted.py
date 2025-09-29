quantidade_pessoas = int(input())
quantidade_media_cervejas = 0
print("Ted se iludiu de novo. Esse é o momento que ele mais precisa dos amigos dele…")
print("Quantos dos amigos dele conseguirão ajudar dessa vez?")

print ("Hora da lista dos amigos da vez!")

if quantidade_pessoas == 0:
    lugar = "MacLaren’s Pub"
    quantidade_media_cervejas = int(input())
    print("Um lugar habitual, mas com uma galera diferente. Será estranho, mas Ted vai.")
    
elif quantidade_pessoas == 1:
    nome_1 = input()
    if nome_1 == "Barney":
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome_1 == "Robin":
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome_1 == "Marshall":
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome_1 == "Lily":
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        print(f"{nome_1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    lugar = input()
    if lugar == "MacLaren’s Pub":
        quantidade_media_cervejas = int(input())
        if (nome_1 == "Barney" or nome_1 == "Lily" or nome_1 == "Marshall" or nome_1 == "Robin"):
            print("Não tem erro, né? Estar no MacLaren’s é como estar em casa.")
        elif (nome_1 != "Barney" and nome_1 != "Lily" and nome_1 != "Marshall" and nome_1 != "Robin"):
            print("Um lugar habitual, mas com uma galera diferente. Será estranho, mas Ted vai.")
    
    if lugar == "Arena de Laser Tag" and nome_1 == "Barney":
        print("Com certeza a Arena de Laser Tag foi escolhida por influência de Barney. Se arrume Ted, é hora de botar um terno, tomar um whisky e partir pra diversão.")
    elif lugar == "Carmichael’s" and nome_1 == "Robin":
        print("Acho que Ted e Robin vão sair em um date… Tomara que Ted não roube aquela trompa azul da parede de novo.")
    
        
elif quantidade_pessoas == 2:
    nome_1 = input()
    if nome_1 == "Barney":
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome_1 == "Robin":
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome_1 == "Marshall":
        
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome_1 == "Lily":
        
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        sem_nome = nome_1
        print(f"{sem_nome} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    nome_2 = input()
    
    if nome_2 == "Barney":
        
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome_2 == "Robin":
       
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome_2 == "Marshall":
       
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome_2 == "Lily":
        
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        sem_nome = nome_2
        print(f"{sem_nome} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    if (nome_1 == "Marshall" or nome_1 == "Lily") and (nome_2 == "Marshall" or nome_2 == "Lily"):
        print("Nada melhor que um casal para dar conselhos de relacionamento.")
    elif (nome_1 == "Barney" or nome_1 == "Marshall") and (nome_2 == "Barney" or nome_2 == "Marshall" ):
        print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.")
    
    lugar = input()
    if lugar == "MacLaren’s Pub":
        quantidade_media_cervejas = int(input())
        if (nome_1 == "Barney" or nome_1 == "Lily" or nome_1 == "Marshall" or nome_1 == "Robin") or (nome_2 == "Barney" or nome_2 == "Lily" or nome_2 == "Marshall" or nome_2 == "Robin") :
            print("Não tem erro, né? Estar no MacLaren’s é como estar em casa.")
        elif (nome_1 != "Barney" and nome_1 != "Lily" and nome_1 != "Marshall" and nome_1 != "Robin") and (nome_2 != "Barney" and nome_2 != "Lily" and nome_2 != "Marshall" and nome_2 != "Robin"):
            print("Um lugar habitual, mas com uma galera diferente. Será estranho, mas Ted vai.")
    
    if lugar == "Arena de Laser Tag" and (nome_1  == "Barney" or nome_2 == "Barney"):
        print("Com certeza a Arena de Laser Tag foi escolhida por influência de Barney. Se arrume Ted, é hora de botar um terno, tomar um whisky e partir pra diversão.")
    elif lugar == "Carmichael’s":
        if nome_1 == "Robin" and (nome_2 != "Barney" and nome_2 != "Lily" and nome_2 != "Marshall" ):
            print("Acho que Ted e Robin vão sair em um date… Tomara que Ted não roube aquela trompa azul da parede de novo.")
        elif nome_2 == "Robin" and (nome_1 != "Barney" and nome_1 != "Lily" and nome_1 != "Marshall" ):
            print("Acho que Ted e Robin vão sair em um date… Tomara que Ted não roube aquela trompa azul da parede de novo.")
    
    
elif quantidade_pessoas == 3:
    
    nome_1 = input()
    
    if nome_1 == "Barney":
       
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome_1 == "Robin":
      
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome_1 == "Marshall":
     
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome_1 == "Lily":
       
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        sem_nome = nome_1
        print(f"{sem_nome} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    nome_2 = input()
    
    if nome_2 == "Barney":
    
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome_2 == "Robin":
     
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome_2 == "Marshall":
  
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome_2 == "Lily":
        
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        sem_nome = nome_2
        print(f"{sem_nome} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    nome_3 = input()
    
    if nome_3 == "Barney":
        
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome_3 == "Robin":
        
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome_3 == "Marshall":
        
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome_3 == "Lily":
     
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        sem_nome = nome_3
        print(f"{nome_3} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
        
    if (nome_1 == "Marshall" or nome_1 == "Lily") and (nome_2 == "Lily" or nome_2 == "Marshall"):
        print("Nada melhor que um casal para dar conselhos de relacionamento.")
    elif(nome_1 == "Marshall" or nome_1 == "Lily") and (nome_3 == "Lily" or nome_3 == "Marshall"):
        print("Nada melhor que um casal para dar conselhos de relacionamento.")        
    elif (nome_2 == "Marshall" or nome_2 == "Lily") and (nome_1 == "Lily" or nome_1 == "Marshall"):
        print("Nada melhor que um casal para dar conselhos de relacionamento.") 
    elif(nome_3 == "Marshall" or nome_3 == "Lily") and (nome_1 == "Lily" or nome_1 == "Marshall"):
        print("Nada melhor que um casal para dar conselhos de relacionamento.") 
    elif (nome_2 == "Marshall" or nome_2 == "Lily") and (nome_3 == "Lily" or nome_3 == "Marshall"):
        print("Nada melhor que um casal para dar conselhos de relacionamento.")   
    elif (nome_3 == "Marshall" or nome_3 == "Lily") and (nome_2 == "Lily" or nome_2 == "Marshall"):
        print("Nada melhor que um casal para dar conselhos de relacionamento.")   
    elif (nome_1 == "Marshall" or nome_1 == "Barney") and (nome_2 == "Barney" or nome_2 == "Marshall"):
        print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.")
    elif(nome_1 == "Marshall" or nome_1 == "Barney") and (nome_3 == "Barney" or nome_3 == "Marshall"):
        print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.")        
    elif (nome_2 == "Marshall" or nome_2 == "Barney") and (nome_1 == "Barney" or nome_1 == "Marshall"):
        print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.") 
    elif(nome_3 == "Marshall" or nome_3 == "Barney") and (nome_1 == "Barney" or nome_1 == "Marshall"):
        print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.") 
    elif (nome_2 == "Marshall" or nome_2 == "Barney") and (nome_3 == "Barney" or nome_3 == "Marshall"):
        print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.")   
    elif (nome_3 == "Marshall" or nome_3 == "Barney") and (nome_2 == "Barney" or nome_2 == "Marshall"):
        print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.")   
    
    lugar = input()
    if lugar == "MacLaren’s Pub":
        quantidade_media_cervejas = int(input())
        if (nome_1 == "Barney" or nome_1 == "Lily" or nome_1 == "Marshall" or nome_1 == "Robin") or (nome_2 == "Barney" or nome_2 == "Lily" or nome_2 == "Marshall" or nome_2 == "Robin") or (nome_3 == "Barney" or nome_3 == "Lily" or nome_3 == "Marshall" or nome_3 == "Robin") :
            print("Não tem erro, né? Estar no MacLaren’s é como estar em casa.")
        elif (nome_1 != "Barney" and nome_1 != "Lily" and nome_1 != "Marshall" and nome_1 != "Robin") and (nome_2 != "Barney" and nome_2 != "Lily" and nome_2 != "Marshall" and nome_2 != "Robin") and (nome_3 != "Barney" and nome_3 != "Lily" and nome_3 != "Marshall" and nome_3 != "Robin"):
            print("Um lugar habitual, mas com uma galera diferente. Será estranho, mas Ted vai.")
    
    if lugar == "Arena de Laser Tag" and (nome_1  == "Barney" or nome_2 == "Barney" or nome_3 == "Barney"):
        print("Com certeza a Arena de Laser Tag foi escolhida por influência de Barney. Se arrume Ted, é hora de botar um terno, tomar um whisky e partir pra diversão.")
    elif lugar == "Carmichael’s":
        if nome_1 == "Robin" and (nome_2 != "Barney" and nome_2 != "Lily" and nome_2 != "Marshall") and (nome_3 != "Barney" and nome_3 != "Lily" and nome_3 != "Marshall"):
            print("Acho que Ted e Robin vão sair em um date… Tomara que Ted não roube aquela trompa azul da parede de novo.")
        elif nome_2 == "Robin" and (nome_1 != "Barney" and nome_1 != "Lily" and nome_1 != "Marshall" ) and (nome_3 != "Barney" and nome_3 != "Lily" and nome_3 != "Marshall"):
            print("Acho que Ted e Robin vão sair em um date… Tomara que Ted não roube aquela trompa azul da parede de novo.")
        elif nome_3 == "Robin" and (nome_1 != "Barney" and nome_1 != "Lily" and nome_1 != "Marshall" ) and (nome_2 != "Barney" and nome_2 != "Lily" and nome_2 != "Marshall"):
            print("Acho que Ted e Robin vão sair em um date… Tomara que Ted não roube aquela trompa azul da parede de novo.")
        
elif quantidade_pessoas == 4:
    nome_1 = input()
    if nome_1 == "Barney":
       
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome_1 == "Robin":
     
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome_1 == "Marshall":
    
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome_1 == "Lily":

        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        sem_nome = nome_1
        print(f"{sem_nome} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")    
    
    nome_2 = input()
    if nome_2 == "Barney":
    
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome_2 == "Robin":
       
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome_2 == "Marshall":
      
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome_2 == "Lily":
    
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        sem_nome = nome_2
        print(f"{nome_2} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    nome_3 = input()
    if nome_3 == "Barney":
       
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome_3 == "Robin":
  
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome_3 == "Marshall":
        
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome_3 == "Lily":
    
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        sem_nome = nome_3
        print(f"{sem_nome} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    
    nome_4 = input()
    
    if nome_4 == "Barney":
     
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome_4 == "Robin":
       
        
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome_4 == "Marshall":
       
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome_4 == "Lily":
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        sem_nome = nome_4
        print(f"{sem_nome} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    #Após isso, será solicitado o lugar que eles vão sair: 
    #Se o lugar escolhido for o MacLaren’s Pub, haverá mais um input, que será a quantidade média de cervejas bebidas pelos que estão presentes:
    
    if (nome_1 == "Marshall" or nome_1 == "Lily") and (nome_2 == "Lily" or nome_2 == "Marshall"):
        print("Nada melhor que um casal para dar conselhos de relacionamento.")
    elif(nome_1 == "Marshall" or nome_1 == "Lily") and (nome_3 == "Lily" or nome_3 == "Marshall"):
        print("Nada melhor que um casal para dar conselhos de relacionamento.")        
    elif (nome_2 == "Marshall" or nome_2 == "Lily") and (nome_1 == "Lily" or nome_1 == "Marshall"):
        print("Nada melhor que um casal para dar conselhos de relacionamento.") 
    elif(nome_3 == "Marshall" or nome_3 == "Lily") and (nome_1 == "Lily" or nome_1 == "Marshall"):
        print("Nada melhor que um casal para dar conselhos de relacionamento.") 
    elif (nome_2 == "Marshall" or nome_2 == "Lily") and (nome_3 == "Lily" or nome_3 == "Marshall"):
        print("Nada melhor que um casal para dar conselhos de relacionamento.")   
    elif (nome_3 == "Marshall" or nome_3 == "Lily") and (nome_2 == "Lily" or nome_2 == "Marshall"):
        print("Nada melhor que um casal para dar conselhos de relacionamento.")   
    elif (nome_1 == "Marshall" or nome_1 == "Barney") and (nome_2 == "Barney" or nome_2 == "Marshall"):
        print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.")
    elif(nome_1 == "Marshall" or nome_1 == "Barney") and (nome_3 == "Barney" or nome_3 == "Marshall"):
        print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.")        
    elif (nome_2 == "Marshall" or nome_2 == "Barney") and (nome_1 == "Barney" or nome_1 == "Marshall"):
        print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.") 
    elif(nome_3 == "Marshall" or nome_3 == "Barney") and (nome_1 == "Barney" or nome_1 == "Marshall"):
        print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.") 
    elif (nome_2 == "Marshall" or nome_2 == "Barney") and (nome_3 == "Barney" or nome_3 == "Marshall"):
        print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.")   
    elif (nome_3 == "Marshall" or nome_3 == "Barney") and (nome_2 == "Barney" or nome_2 == "Marshall"):
        print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.")   
    elif (nome_1 == "Marshall" or nome_1 == "Robin" or nome_1 == "Lily" or nome_1 == "Barney") and (nome_2 == "Marshall" or nome_2 == "Robin" or nome_2 == "Lily" or nome_2 == "Barney") and (nome_3 == "Marshall" or nome_3 == "Robin" or nome_3 == "Lily" or nome_3 == "Barney") and (nome_4 == "Marshall" or nome_4 == "Robin" or nome_4 == "Lily" or nome_4 == "Barney"):
        print("O quinteto estará reunido nessa jornada! É o momento perfeito pra brincar de “Você conhece o Ted?")
    
    lugar = input()
    if lugar == "MacLaren’s Pub":
        quantidade_media_cervejas = int(input())
        if (nome_1 == "Barney" or nome_1 == "Lily" or nome_1 == "Marshall" or nome_1 == "Robin") or (nome_2 == "Barney" or nome_2 == "Lily" or nome_2 == "Marshall" or nome_2 == "Robin") or (nome_3 == "Barney" or nome_3 == "Lily" or nome_3 == "Marshall" or nome_3 == "Robin") or (nome_4 == "Barney" or nome_4 == "Lily" or nome_4 == "Marshall" or nome_4 == "Robin") :
            print("Não tem erro, né? Estar no MacLaren’s é como estar em casa.")
        elif (nome_1 != "Barney" and nome_1 != "Lily" and nome_1 != "Marshall" and nome_1 != "Robin") and (nome_2 != "Barney" and nome_2 != "Lily" and nome_2 != "Marshall" and nome_2 != "Robin") and (nome_3 != "Barney" and nome_3 != "Lily" and nome_3 != "Marshall" and nome_3 != "Robin") and (nome_4 != "Barney" and nome_4 != "Lily" and nome_4 != "Marshall" and nome_4 != "Robin"):
            print("Um lugar habitual, mas com uma galera diferente. Será estranho, mas Ted vai.")
    
    if lugar == "Arena de Laser Tag" and (nome_1  == "Barney" or nome_2 == "Barney" or nome_3 == "Barney"):
        print("Com certeza a Arena de Laser Tag foi escolhida por influência de Barney. Se arrume Ted, é hora de botar um terno, tomar um whisky e partir pra diversão.")
    elif lugar == "Carmichael’s":
        if nome_1 == "Robin" and (nome_2 != "Barney" and nome_2 != "Lily" and nome_2 != "Marshall") and (nome_3 != "Barney" and nome_3 != "Lily" and nome_3 != "Marshall") and (nome_4 != "Barney" and nome_4 != "Lily" and nome_4 != "Marshall") :
            print("Acho que Ted e Robin vão sair em um date… Tomara que Ted não roube aquela trompa azul da parede de novo.")
        elif nome_2 == "Robin" and (nome_1 != "Barney" and nome_1 != "Lily" and nome_1 != "Marshall" ) and (nome_3 != "Barney" and nome_3 != "Lily" and nome_3 != "Marshall") and (nome_4 != "Barney" and nome_4 != "Lily" and nome_4 != "Marshall"):
            print("Acho que Ted e Robin vão sair em um date… Tomara que Ted não roube aquela trompa azul da parede de novo.")
        elif nome_3 == "Robin" and (nome_1 != "Barney" and nome_1 != "Lily" and nome_1 != "Marshall" ) and (nome_2 != "Barney" and nome_2 != "Lily" and nome_2 != "Marshall") and (nome_4 != "Barney" and nome_4 != "Lily" and nome_4 != "Marshall"):
            print("Acho que Ted e Robin vão sair em um date… Tomara que Ted não roube aquela trompa azul da parede de novo.")
        elif nome_4 == "Robin" and (nome_1 != "Barney" and nome_1 != "Lily" and nome_1 != "Marshall" ) and (nome_2 != "Barney" and nome_2 != "Lily" and nome_2 != "Marshall") and (nome_3 != "Barney" and nome_3 != "Lily" and nome_3 != "Marshall"):
            print("Acho que Ted e Robin vão sair em um date… Tomara que Ted não roube aquela trompa azul da parede de novo.")
        
        
if quantidade_pessoas == 0:
    print()
    print("Relatório da situação de Ted:")
    print("- Ted foi para o MacLaren’s… Olhe em volta, Ted, você está sozinho.")   
    print(f"Quantidade de cervejas bebidas por Ted:{quantidade_media_cervejas} cervejas.")
else:           
    if quantidade_pessoas == 1 :
        print()
        print("Relatório da situação de Ted:")
        print(f"- Ted foi consolado por: {nome_1}.")
        print(f"O local de afogar as mágoas foi: {lugar}.")
        print("- Saideira de um pra um. Nada melhor do que uma pessoa pra ouvir seus problemas")
        print("Quantidade de cervejas bebidas pelo grupo:")
        if lugar == "MacLaren’s Pub":
            total_cerveja = quantidade_media_cervejas 
            print("Quantidade de cervejas bebidas pelo grupo:")
            print(f"{total_cerveja} cervejas.")
        print("Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?")

    elif quantidade_pessoas == 2:
        print()
        print("Relatório da situação de Ted:")
        print(f"- Ted foi consolado por: {nome_1} e {nome_2}.")
        print(f"- O local de afogar as mágoas foi: {lugar}.")
        print("- Duas pessoas se compadeceram com a situação do pobre Ted.")
        if lugar == "MacLaren’s Pub":
            total_cerveja = quantidade_media_cervejas * 2
            print("Quantidade de cervejas bebidas pelo grupo:")
            print(f"{total_cerveja} cervejas.")
        print("Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?")

    elif quantidade_pessoas == 3:
        print()
        print("Relatório da situação de Ted:")
        print(f"- Ted foi consolado por: {nome_1}, {nome_2} e {nome_3}.")
        print(f"- O local de afogar as mágoas foi: {lugar}.")
        print("- Três pessoas! Ted conseguiu se divertir bastante.")
        if lugar == "MacLaren’s Pub":
            total_cerveja = quantidade_media_cervejas * 3
            print("Quantidade de cervejas bebidas pelo grupo:")
            print(f"{total_cerveja} cervejas.")
        print("Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?")

    elif quantidade_pessoas == 4:
        print()
        print("Relatório da situação de Ted:")
        print(f"- Ted foi consolado por: {nome_1}, {nome_2}, {nome_3} e {nome_4}.")
        print(f"- O local de afogar as mágoas foi: {lugar}.")
        print("- O quinteto junto consegue resolver qualquer problema!")
        if lugar == "MacLaren’s Pub":
            total_cerveja = quantidade_media_cervejas * 4
            print("Quantidade de cervejas bebidas pelo grupo:")
            print(f"{total_cerveja} cervejas.")
        print("Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?")
    else:
        print()
        print("Relatório da situação de Ted:")
        print(f"- Ted foi consolado por: {nome_1}, {nome_2}, {nome_3} e {nome_4}.")
        print(f"- O local de afogar as mágoas foi: {lugar}.")
        print("- Saiu um quinteto um pouco diferente do que a gente tá acostumado, mas no fim conseguiram deixar Ted alegre.")
        total_cerveja = quantidade_media_cervejas * 4
        if lugar == "MacLaren’s Pub":
            print("Quantidade de cervejas bebidas pelo grupo:")
            print(f"{total_cerveja} cervejas.")
        print("Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?")
        

