print ("Ativando a máquina...")

nome = input().capitalize()
ano = int(input())
confiavel = 0

#se confiavel for = 1 então a previsão é confiavel
#se confiavel for = 0 então é inconfiavel
if ano % len(nome) == 0:
    confiavel = 1 
else:
    confiavel = 0

if confiavel == 1 and nome == ("Frink"):
    print("Professor Frink irá inventar o rebigulador?! A máquina deve estar com defeito! Glavin!")
else:
    if confiavel == 1 and nome != ("Frink"):
        print(f"Previsão confiável! O rebigulador será real em {ano}!")
    else:
        if confiavel == 0 and nome == ("Frink"):
            print("Nem precisava colocar os dados! O rebigulador jamais existiria em qualquer universo!")
        else:
            if confiavel == 0 and nome != ("Frink"): 
                print(f"Previsão instável! {nome} também deve achar que o rebigulador é ridículo...")