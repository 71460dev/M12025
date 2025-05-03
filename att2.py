nome = input('Digite o nome do aluno: ')
print ('Seja bem-vindo' ,nome , 'Vamos calcular seu media Aritmética! ')

nota1 = float(input("Digite a primeira nota (0 a 10): "))
while nota1 < 0 or nota1 > 10:
    print("Nota inválida! Digite um valor entre 0 e 10.")
    nota1 = float(input("Digite a primeira nota (0 a 10): "))

nota2 = float(input("Digite a segunda nota (0 a 10): "))
while nota2 < 0 or nota2 > 10:
    print("Nota inválida! Digite um valor entre 0 e 10.")
    nota2 = float(input("Digite a segunda nota (0 a 10): "))

media = (nota1 + nota2) / 2
print ('Sua Media é: ',media)

if media >= 6:
    print("Situação: APROVADO")
else:
    print("Situação: REPROVADO")