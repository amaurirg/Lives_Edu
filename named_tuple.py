from collections import namedtuple



n_t = namedtuple('Jogador', ['Nome', 'Time', 'Camisa'])

j_0 = n_t('Ronaldo', 'Brasil', 9)
j_1 = n_t('Neymar', 'PSG', 10)

lista_jogadores = [j_0, j_1]

for jogador in lista_jogadores:
	print('\nNome do Jogador:', jogador.Nome)
	print('Time de atuação:', jogador.Time)
	print('Número da camisa:', jogador.Camisa)
