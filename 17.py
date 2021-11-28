import math
area = float(input('Digite o tamanho em metros quadrados da area a ser pintada: '))
litros = area/6
latas = math.ceil(litros/18)
galoes = math.ceil(litros/3.6)
print('Latas:',latas)
print('Preco apenas com latas:',latas*80,'R$\n')
print('Galoes:',galoes)
print('Preco apenas com galoes:',galoes*25,'R$\n')
latas=0
while(galoes>5):
    galoes -= 5
    latas += 1
print('Latas:',latas)
print('Galoes:',galoes)
print('Preco com latas e galoes:',latas*80 + galoes*25,'R$\n')
