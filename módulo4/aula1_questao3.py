n1=float(input("Digite um número: "))
n2=float(input("Digite um número: "))
n3=float(input("Digite um número: "))
media= float(n1+n2+n3)/3
if media>=60:
    print(f" Média: {media:.2f} , Aprovado")
    print("Fim") 
if media>=40 and  media<60:
    print(f" Média: {media:.2f} ,Recuperação")
    print("Fim") 
if media <60:
    print(f" Média: {media:.2f} ,Reprovado")
    print("Fim") 
    