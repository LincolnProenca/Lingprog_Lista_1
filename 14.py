peso = float(input('Insira o peso: '))
excesso = 0
if (peso > 4):
    excesso = peso-50
multa = int(excesso)*4
print('Peso:',peso)
print('Excesso:',excesso)
print('Multa:',multa)


