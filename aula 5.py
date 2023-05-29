def area(largura, comprimento):
    total = largura * comprimento
    return total

largura = int( input("Digite a Largura: ") )
comprimento = int( input("Digite o comprimento: ") )

print("Sua area total e:", area(largura, comprimento), "m2")