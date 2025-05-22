print('R$60,00 reais por dia e R$0,15 centavos por km rodado')
km = float(input('Quantos km foram percorridos? '))
d = int(input('Quantos dia ficou com o carro? '))

print('Voce deve R${} reais, por km rodado e R${} reais, por dias alugados'
      ' e no total R${} reais'.format(km*0.15,d*60,(km*0.15)+(d*60)))
