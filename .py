frase = input ("escreva uma frase  ")
frase_dividida = frase.split()
for palavrinha in frase_dividida:
    print(palavrinha[::-1])

lista = [palavrinha]
print(lista)