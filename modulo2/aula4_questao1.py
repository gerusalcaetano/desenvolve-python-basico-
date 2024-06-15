#Questão 1
comprimento = float(input("Digite o comprimento do seu terreno:"))
largura = float(input("Digite a largura do seu terreno:"))
preco_m2 = float(input("Digite o preço do metro quadrado: "))
area_m2 = comprimento * largura
preco_total = preco_m2 * area_m2
print(f"O terreno possui {area_m2}m² e custa R${preco_total:,.2f}")
