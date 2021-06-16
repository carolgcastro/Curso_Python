l = float(input('Qual é a largura da parede em metros? '))
a = float(input('Qual é a altura da parede em metros? '))

mq = l * a

litro = mq / 2

print('Para {}m² você usará {} litros de tinta.'.format(mq, litro))
