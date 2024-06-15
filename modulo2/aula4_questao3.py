#Produto 1
p1= str(input("Digite o nome do produto 1: "))
v1= float(input("Digite o preço unitário do produto 1: "))
q1= int(input("Digite a quantidade do produto 1:" ))
#Produto 2
p2= str(input("Digite o nome do produto 2: "))
v2= float(input("Digite o preço unitário do produto 2: "))
q2= int(input("Digite a quantidade do produto 2:" ))
#Produto 3
p3= str(input("Digite o nome do produto 3: "))
v3= float(input("Digite o preço unitário do produto 3: "))
q3= int(input("Digite a quantidade do produto 3:" ))
total = (v1*q1)+(v2*q2)+(v3*q3)
print (f"Total: R$ {total:,.2f}")