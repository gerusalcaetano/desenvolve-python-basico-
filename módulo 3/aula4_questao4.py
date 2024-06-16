
distancia = float (input ("Digite a distância : "))
peso = float (input ("Digite o peso do pacote : "))
if ((distancia <= 100 ) and peso <= 10) : 
    print(f"Valor a ser pago: {peso*1:.2f}") 
if (distancia >= 100 and distancia <= 300):  
    print(f"Valor a ser pago:  {peso*1.5:.2f}")
if distancia >= 300  and peso <= 10:  
     print(f"Valor a ser pago:  {peso*2:.2f}")
if  peso >= 10:  
     peso_com_taxa = peso + 10.00
     print(f"Taxa de peso adicionada, totalizando: {peso_com_taxa:.2f}")
