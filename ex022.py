n = input('Digite Seu nome Completo: ')
mais = n.upper()
min = n.lower()
lc = len(n) - n.count(' ')
pn = n.split()[0]
lp = len(n.split()[0])
print('O nome maiusculo fica: {}\n'
      'Minusculo fica: {}\n'
      'Tem {} letras\n'
      'O primeiro nome é {} e tem {} letras'.format(mais,min,lc,pn,lp))


