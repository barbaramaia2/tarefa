peso = float(input("Digite seu peso"))
altura = float(input("Digite sua altura"))

imc = peso/(altura**2)

if imc <= 18.5:
    print("abaixo do peso")
elif 18.5 <imc <25:
    print("Peso Normal")
elif 25 <imc <30:
    print("Acima do peso")
else:
    print("Obeso")
    