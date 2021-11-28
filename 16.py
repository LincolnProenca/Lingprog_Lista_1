import math
area = float(input('Digite o tamanho em metros quadrados da area a ser pintada: '))
latas = math.ceil((area/54))
print('Quantidade de latas a serem compradas:',latas)
print('Preco total:',latas*80,'R$')
