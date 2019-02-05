#Um Programa que calcula equações do 2o grau

'''
Formula de Baskara
x * * 2 + x + nun = 0
delt = B * * 2 + 4ac
x = -(b) + -{raiz delta} / 2a
author: Victor D.C.C
'''

#Imports


# Variables and Execution

a = int(input('Digite o Elemento A da equação: '))
b = int(input('Digite o Elemento B da equação: '))
c = int(input('Digite o Elemento C da equação: '))
print(' ')

delt = (b * * 2) - (4 * a * c)
print('Delta = {}² - 4 * {} * {}'.format(b, a, c))
print('Delta = {}'.format(delt))

if delt < 0:
    print('Essa equação não possui raizes em numeros reais. : :DD')
	print('Tente outra equação.')

if delt > 0:
    raizd = (delt * * 0.5)
	down_equação = 2 * a
	print(' ')
	print('X = -({}) +- (RAIZ {}) / 2a'.format(b, delt))
	print(' ')
	x1 = (-(b) + raizd) / down_equação
	x2 = (-(b) - raizd) / down_equação
	print('X1 = {}'.format(x1))
	print('X2 = {}'.format(x2))
else:
    print('Sua equação é Linear e só possui uma Raiz:')
	print(' ')
	down_equação = 2 * a
	xlin = (-(b))
	print('X = {}/{}'.format(xlin, down_equação))

'''
X = -(b) - +(raiz delta) / 2 a 
'''