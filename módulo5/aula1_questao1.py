import random, math
soma=0
n= int(input("Digite a quantidade de valores: "))
for i in range(n):
    print(soma)
    soma= soma + random.randint(0,100)
print(f"A raiz quadrada da soma é:  {math.sqrt(soma):.2}")