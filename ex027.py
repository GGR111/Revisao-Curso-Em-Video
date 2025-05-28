n = input('Digite seu nome completo: ').strip().capitalize()
e = n.count(' ')+1
print('Muito prazer\n'
      'Primeiro nome: {}\n'
      'Ultimo nome: {}'.format(n[0].split(),n[0+e].split()))
