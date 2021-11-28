a = float(input('Digite o quanto ganha por hora: '))
b = int(input('Digite o numero de horas trabalhadas no mes: '))
bruto = a*b
ir = bruto*0.11
inss = bruto*0.08
liquido = bruto - ir - inss
print('Salario bruto:',bruto,'R$')
print('IR (11%):',ir,'R$')
print('INSS (11%):',inss,'R$')
print('Salario Liquido:',liquido,'R$')