from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
h = hypot(co,ca)
print('Cateto oposto: {}'
      ' Cateto Adjacente: {} e a hipotenusa: {:.2f}'.format(co,ca,h))