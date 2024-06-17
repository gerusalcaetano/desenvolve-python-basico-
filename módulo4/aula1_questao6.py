n=int(input("Digite a quantidade de experimentos "))
cont=0
soma_sapo, soma_rato, soma_coelho=0,0,0
cobaias=soma_sapo +soma_coelho + soma_rato
while cont<n:
    quantia= int(input("Digite a quantidade de animais no experimento:"))
    tipo=input(("Digite o tipo:"))
    cont=cont+1
    if tipo=="s":
        soma_sapo=soma_sapo + quantia
    elif tipo=="r":
        soma_rato=soma_rato + quantia
    elif tipo=="c":
        soma_coelho=soma_coelho + quantia
print("Total de cobaiais: ", soma_sapo +soma_coelho + soma_rato)
print("Total de sapos:", soma_sapo)
print("Porcentagem de sapos:", soma_sapo* (soma_sapo +soma_coelho + soma_rato)/100)
print("Total de coelhos:", soma_coelho)
print("Porcentagem de coelhos:", soma_coelho* (soma_sapo +soma_coelho + soma_rato)/100)
print("Total de ratos:", soma_rato)
print("Porcentagem de ratos:", soma_rato* (soma_sapo +soma_coelho + soma_rato)/100)


    
    