N = int(input())
bloco = 1
braille_blank = "\u2800"  

total = N

for i in range(N):
    hashtag = "#"
    espacos = total - i - 1  
    print(braille_blank * espacos + hashtag * bloco)
    bloco = bloco + 2