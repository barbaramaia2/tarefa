altura = float(input("Digite sua altura"))
sexo = input("Digite F ou M")

if sexo== "F":
    peso_ideal = (62.7 * altura) - 44.7
    print("O peso ideal para uma mulher com altura metros de altura e peso_ideal Kg")

elif sexo =="M":
    peso_ideal =(72.7 * altura) - 58
    print("O peso ideal do homem com altura metros de altura e peso_ideal Kg")