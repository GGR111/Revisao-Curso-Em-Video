f = input('Digite um frase: ').strip().lower()
print('A letra "A" apareceu {} vezes'.format(f.count('a')))
print('A primeir letra "A" apareceu na posição {} pela primeira vez'.format(f.find('a')+1))
print('A ultima vez que aparece a letra A é na posição {}'.format(f.rfind('a')+1))