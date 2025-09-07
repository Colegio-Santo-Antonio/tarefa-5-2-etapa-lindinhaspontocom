# Leia uma linha com o número do cartão
numero = input().strip()
digitos = [int(i) for i in numero]
ímpares = digitos[-1::-2]
pares = digitos[-2::-2]
pares_dobrados = []
for d in pares:
  dobro = d * 2
  if dobro > 9:
      dobro -= 9
    pares_dobrados.append(dobro)
total = sum(impares) + sum(pares_dobrados)
if total % 10 == 0:
    print("cartão válido")
else:
    print("cartão inválido")
  

