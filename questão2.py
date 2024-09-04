valor1 = 0
valor2 = 1
inserir = int(input("Insira um numero para verificarmos se ele pertence a sequência fibonacci: "))

while valor1 < inserir:
    valor1, valor2 = valor2, valor1 + valor2

if valor1 == inserir:
    print(f"{inserir} faz parte da sequência fibonacci!")
else:
    print(f"{inserir} não faz parte da sequência fibonacci!")
