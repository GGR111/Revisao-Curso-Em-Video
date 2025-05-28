n = int(input('Digite um numero inteiro no maximo 4 digitos: '))
un = n // 1 % 10
de = n // 10 % 10
ce = n // 100 % 10
mi = n // 1000 % 10

print('Numero: {}\n'
      'Unidade: {}\n'
      'Dezena: {}\n'
      'Centena: {}\n'
      'Milhar: {}'.format(n,un,de,ce,mi))
