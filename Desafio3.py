salario = float( input("Informe seu Salário: ") )

reajuste1 = float(10)
reajuste2 = float(15)

aumento = salario*reajuste1/100
Aumento = salario*reajuste2/100
salariofinal = salario + aumento
Salariofinal = salario + Aumento

if salario > 8250:
    print("Seu salário final é: ",salariofinal)
else:
    print("Seu Salário final é: ",Salariofinal)