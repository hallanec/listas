#Input
#Inicialmente será fornecida a quantidade de pessoas que sairão com Ted:

quantidade_pessoas = int(input())

#Em seguida, a quantidade de inputs que serão feitos para receber o nome das pessoas será a mesma da quantidade definida no primeiro input (Será entre 0 e 4)
#Obs.: Caso a quantidade de pessoas fornecida seja 0, Ted irá direto para o MacLaren’s Pub, portanto, não haverá as entradas de nomes nem de lugar, mas haverá a entrada da quantidade média de cervejas (que ele irá beber sozinho).

#O programa deve iniciar com a seguinte saída:
#Ted se iludiu de novo. Esse é o momento que ele mais precisa dos amigos dele…

print("Ted se iludiu de novo. Esse é o momento que ele mais precisa dos amigos dele…")
print("Quantos dos amigos dele conseguirão ajudar dessa vez?")

##Agora sobre os nomes fornecidos:
#Antes de pedir os nomes, printe:

print ("Hora da lista dos amigos da vez!")

#Antes de pedir os nomes, printe:

#Hora da lista dos amigos da vez!

#Se o nome digitado for Barney:
#Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.

#Se o nome digitado for Robin:
#Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.

#Se o nome digitado for Marshall:
#O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.

#Se o nome digitado for Lily:
#Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.

#Já se o nome digitado for qualquer outro, printe:
#{Nome da pessoa} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.

## APÓS RECEBER OS NOMES


#Se apenas os nomes de Marshall e Lily forem fornecidos:
#Nada melhor que um casal para dar conselhos de relacionamento.

#Se apenas os nomes de Barney e Marshall foram fornecidos:
#Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.

#Se forem fornecidos o nome de todos os 4 protagonistas (Barney, Robin, Marshall e Lily):

#O quinteto estará reunido nessa jornada! É o momento perfeito pra brincar de “Você conhece o Ted?”.

if quantidade_pessoas == 0:
    lugar = "MacLaren’s Pub"
elif quantidade_pessoas == 1:
    nome_1 = input()
    if nome_1 == "Barney":
        Barney = nome_1
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome_1 == "Robin":
        Robin = nome_1
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome_1 == "Marshall":
        Marshall = nome_1
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome_1 == "Lily":
        Lily = nome_1
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        print(f"{nome_1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    #Após isso, será solicitado o lugar que eles vão sair: 
    #Se o lugar escolhido for o MacLaren’s Pub, haverá mais um input, que será a quantidade média de cervejas bebidas pelos que estão presentes:
    
    lugar = input()
    if lugar == "MacLaren’s Pub":
        quantidade_media_cerverjas = input()
elif quantidade_pessoas == 2:
    nome_1 = input()
    if nome_1 == "Barney":
        Barney = nome_1
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome_1 == "Robin":
        Robin = nome_1
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome_1 == "Marshall":
        Marshall = nome_1
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome_1 == "Lily":
        Lily = nome_1
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        sem_nome = nome_1
        print(f"{sem_nome} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    nome_2 = input()
    
    if nome_2 == "Barney":
        Barney = nome_2
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome_2 == "Robin":
        Robin = nome_2
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome_2 == "Marshall":
        Marshall = nome_2
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome_2 == "Lily":
        Lily = nome_2
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        sem_nome
        print(f"{sem_nome} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    if (nome_1 == "Marshall" or nome_1 == "Lily") and (nome_2 == "Marshall" or nome_2 == "Lily"):
        print("Nada melhor que um casal para dar conselhos de relacionamento.")
    elif (nome_1 == "Barney" or nome_1 == "Marshall") and (nome_2 == "Barney" or nome_2 == "Marshall" ):
        print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.")
    
    #Após isso, será solicitado o lugar que eles vão sair: 
    #Se o lugar escolhido for o MacLaren’s Pub, haverá mais um input, que será a quantidade média de cervejas bebidas pelos que estão presentes:
    
    
    lugar = input()
    if lugar == "MacLaren’s Pub":
        quantidade_media_cerverjas = input()
elif quantidade_pessoas == 3:
    
    nome_1 = input()
    
    if nome_1 == "Barney":
        Barney = nome_1
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome_1 == "Robin":
        Robin = nome_1
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome_1 == "Marshall":
        Marshall = nome_1
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome_1 == "Lily":
        Lily = nome_1
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        sem_nome = nome_1
        print(f"{sem_nome} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    nome_2 = input()
    
    if nome_2 == "Barney":
        Barney = nome_2
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome_2 == "Robin":
        Robin = nome_2
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome_2 == "Marshall":
        Marshall = nome_2
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome_2 == "Lily":
        Lily = nome_2
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        sem_nome = nome_2
        print(f"{sem_nome} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    nome_3 = input()
    
    if nome_3 == "Barney":
        Barney = nome_3
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome_3 == "Robin":
        Robin = nome_3
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome_3 == "Marshall":
        Marshall = nome_3
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome_3 == "Lily":
        Lily = nome_3
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        sem_nome = nome_3
        print(f"{nome_3} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
        
    if (nome_1 == "Marshall" or nome_1 == "Lily") and (nome_2 == "Lily" or nome_2 == "Marshall")
        print("Nada melhor que um casal para dar conselhos de relacionamento.")
    #Após isso, será solicitado o lugar que eles vão sair: 
    #Se o lugar escolhido for o MacLaren’s Pub, haverá mais um input, que será a quantidade média de cervejas bebidas pelos que estão presentes:
    
    lugar = input()
    if lugar == "MacLaren’s Pub":
        quantidade_media_cerverjas = input()
elif quantidade_pessoas == 4:
    nome_1 = input()
    if nome_1 == "Barney":
        Barney = nome_1
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome_1 == "Robin":
        Robin = nome_1
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome_1 == "Marshall":
        Marshall = nome_1
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome_1 == "Lily":
        Lily = nome_1
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        sem_nome = nome_1
        print(f"{sem_nome} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")    
    
    nome_2 = input()
    if nome_2 == "Barney":
        Barney = nome_2
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome_2 == "Robin":
        Robin = nome_2
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome_2 == "Marshall":
        Marshall = nome_2
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome_2 == "Lily":
        Lily = nome_2
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        sem_nome = nome_2
        print(f"{nome_2} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    nome_3 = input()
    if nome_3 == "Barney":
        Barney = nome_3
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome_3 == "Robin":
        Robin = nome_3
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome_3 == "Marshall":
        Marshall = nome_3
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome_3 == "Lily":
        Lily = nome_3
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        sem_nome = nome_3
        print(f"{sem_nome} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    
    nome_4 = input()
    
    if nome_4 == "Barney":
        Barney = nome_4
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome_4 == "Robin":
        Robin = nome_4
        
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome_4 == "Marshall":
        Marshall = nome_4
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome_4 == "Lily":
        Lily = nome_4
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        sem_nome = nome_4
        print(f"{sem_nome} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    #Após isso, será solicitado o lugar que eles vão sair: 
    #Se o lugar escolhido for o MacLaren’s Pub, haverá mais um input, que será a quantidade média de cervejas bebidas pelos que estão presentes:
    lugar = input()
    if lugar == "MacLaren’s Pub":
        quantidade_media_cerverjas = input()
    

