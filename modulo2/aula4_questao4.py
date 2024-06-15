#Leitura de dados
valor= int(input("Digite a quantia em reais:  "))
#Processamento
nota100=valor//100
valor=valor % 100

nota50=valor//50
valor=valor % 50
nota20=valor//20
valor=valor % 20
nota10=valor//10
valor=valor % 10
nota5=valor/5
valor=valor % 5
nota2=valor//2
valor=valor % 2
nota1=valor
#Impressão de dados- saída
print("Saída: ")
print(f"{nota100} notas de R$100,00, ")
print(f"{nota50} notas de R$ 50,00")
print(f"{nota20} notas de R$20,00")
print(f"{nota10} notas de R$10,00")
print(f"{nota5} notas de R$5,00")
print(f"{nota2} notas de R$2,00")
print(f"{nota1} notas de R$1,00")
