palavra = []
palavra = input("Digite uma palavra: ")
cont = 0

for i in list(palavra):
    if i == 'a':
        cont = cont + 1
        
if cont > 0:
    print (f"A palavra '{palavra}' tem {cont} letra(s) 'A'.")
else:
    print(f"A palavra '{palavra}' não tem letra A.")