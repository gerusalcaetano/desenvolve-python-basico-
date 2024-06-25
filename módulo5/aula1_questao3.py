import random
soma=0
cont=0
n1= int(input("Adivinhe o número entre 1 e 10: "))
if n1>10:
    print("Muito alto, tente novamente!")
else:
      print("Seu número escolhido foi:", n1)
adv= int(random.randint(1,10))
if n1==adv:
    print(f"Correto! O número é:{adv}")
else:
    print(f"Errou! O número é:{adv}")