from random import randint
computador = randint(0,10)
print('Sou seu computador... acabei de pensar em um número entre 1 e 1000.')
print('Tente adivinhar')
acertou = false
while not acertou:
	jogador = int(input('Qual o seu palpite?')
	if jogador == computador:
	acertou = True
print('Acertou')