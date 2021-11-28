a = float(input('Insira o tamanho do arquivo em MB: '))
b = float(input('Insira a velocidade da internet em Mb/s: '))
print('O tempo aproximado de download e',(a*8)/(b*60),'minutos')