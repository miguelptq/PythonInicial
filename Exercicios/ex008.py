# Guardar kms Percorridos e o numero de dias de aluguer
kmPercorridos = float(input("Quantos kms foram percorrids: "))
diasAluguer = int(input("Dias de aluguer: "))

# Variaveis de calculo
custoDia = 60
custoKm = 0.456

# Calcular preco

preco = kmPercorridos * custoKm + diasAluguer * custoDia
# Exibir valor a pagar
print(f"Total a pagar: {preco}")