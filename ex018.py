""" 30º  45º  60º
sen 1/2 √2/2 √3/2
cos √3/2 √2/2 1/2
tan √3/3  1   √3
"""
from math import sin, cos, tan, radians
a = float(input('Digite um angulo qualquer: '))
print('Angulo {}\n'
      'Seno: {:.2f}\n'
      'Cosseno: {:.2f}\n'
      'Tangente: {:.2f}'.format(a,sin(radians(a)),cos(radians(a)),tan(radians(a))))
