n1 = int(input("Em que ano voce está? "))
n2 = int(input("E qual foi o ano do seu nascimento? "))
n3 = n1 - n2
if n3 >= 18:
    print("Pode tirar a CNH ")
if n3 < 18:
    print("Não pode tirar a sua CNH ")