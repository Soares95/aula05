dentro=0
fora=0
for a in range(10):
    n = int(input("Digite um numero :"))
if n>=10 and n<=20:
    dentro = dentro + 1
    print("numeros de dentro")
else:
    fora= fora+1
    print(dentro, fora)