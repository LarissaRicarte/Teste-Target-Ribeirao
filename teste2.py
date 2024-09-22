palavra = []
palavra = input("Digite uma palavra: ")
cont = 0

for i in list(palavra):
    if i == 'a':
        cont = cont + 1

print (f"A palavra {palavra} tem {cont} letra(s) 'A'.")