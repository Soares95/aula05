n = int(input("Digite um numero\n"
                "só será permitido numero maior que zero\n"
                "qual o nuemro: "))
if n >= 0:
    for a in range(1,n+1,1):
        print(a)
else:
    print("numero invalido")