anoAtual = int(input())
salarioBase = 1000.00
aumentoBase = 0.015
anoBase = 2007
if (anoAtual < 2006):
    print("o ano informado deverá ser  2005!", end="\n")
else:
    if (anoAtual == 2006):
        salarioAtual = salarioBase + (salarioBase * aumentoBase)
    else:
        salarioAtual = salarioBase + (salarioBase * aumentoBase)
        for anoBase in range(2007, anoAtual + 1):
            aumentoBase += 0.010
            salarioAtual = salarioAtual + (salarioAtual * aumentoBase)
    print(f"Salário atual: R${salarioAtual}", end="\n")