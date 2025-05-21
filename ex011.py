l1 = float(input('Digite quantos metros tem a base da parede: '))
l2 = float(input('Digite quantos metros tem a lado da parede: '))
print('-='*20)
print('Com a base da parede medindo {}m e a a altura {}m\n'
      'temos a area de {:.2f}m²\n'
      'sabendo que 1 litro de tinta pinta 2m²\n'
      'precisaremos de {:.2f} litros de tinta'.format(l1,l2,l1*l2,(l1*l2)/2))
print('-='*20)