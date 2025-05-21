s = float(input('Seu salario: '))
r = s + (s * (15/100))
print('antes seu salario era R${} reais'
      ' agora seu salario é R${:.2f} reais'.format(s,r))