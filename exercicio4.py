def calcular_area(figura,parametro1,parametro2):
    if figura=="circulo":
        return float(parametro1)*int(parametro2)*int(parametro2)
    if figura=="rectangulo":
        return int(parametro1)*int(parametro2)
    if figura=="triangulo":
        return int(parametro1)*int(parametro2)/2

figura = input ("escreva aqui qual a figura")
parametro1 = input ("escreva aqui o primeiro parametro1 (se for circulo adicionar 3.14)")
parametro2 = input("escreva aqui o segundo parametro2")

print(calcular_area(figura,parametro1,parametro2))
