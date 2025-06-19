num = 7

palpite = int(input('Tente adivinhar o número entre 1 e 10: '))

while palpite != num:
    print('Você errou! Tente novamente.')
    palpite = int(input('Tente adivinhar o número entre 1 e 10: '))

print('Parabéns! Você acertou o número!')