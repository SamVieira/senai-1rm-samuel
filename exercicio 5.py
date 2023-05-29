print("Qual o valor do salario?")
salario = float(input())

print("Qual sera o aumento salarial")
porcentagem = float(input())

aumento = salario*porcentagem/100
salariofinal = salario + aumento

print("Salário atual: R$",salario)
print("\n0 valor do aumento sera R$",aumento)
print("O valor do salário com reajuste será: R$",salariofinal)