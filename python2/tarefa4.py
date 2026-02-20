n1 = float(input("O seu salário é de: "))
if n1 > 1250:
    print(f"O seu novo salário é: {n1 * 1.10:.2f}")
if n1 < 1250:
    print(f"O seu novo salário é: {n1 * 1.15:.2f}")
