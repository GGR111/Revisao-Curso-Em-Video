co = float(input('Digite o Cateto oposto: '))
ca = float(input('Digite o Cateto adjacente: '))
h = ((co**2)+(ca**2))**0.5
print('Com o cateto oposto de {} e'
      ' o adjacente de {} temos a hipotenusa de {:.2f}'.format(co,ca,h))