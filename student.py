# Leia uma linha com o número do cartão
numero = input().strip()

# Transforma em lista de inteiros
digitos = [int(i) for i in numero]

# Dígitos ímpares (da direita para a esquerda, de 2 em 2)
impares = digitos[-1::-2]

# Dígitos pares (da direita para a esquerda, de 2 em 2)
pares = digitos[-2::-2]

# Dobra os pares e ajusta se passar de 9
pares_dobrados = []
for d in pares:
    dobro = d * 2
    if dobro > 9:
        dobro -= 9
    pares_dobrados.append(dobro)

# Soma tudo
total = sum(impares) + sum(pares_dobrados)

# Verificação final (atenção às maiúsculas e acentos!)
if total % 10 == 0:
    print("Cartão válido")
else:
    print("Cartão inválido")
