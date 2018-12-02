import sys

# Algoritmo FCFS
def FCFS(fila, cabecote):
	fila.insert(0, cabecote)

	atendidos = []
	cilindros = 0

	for i in range(len(fila) - 1):
		c = max(int(fila[i]), int(fila[i+1])) - min(int(fila[i]), int(fila[i+1]))
		cilindros += c

	for f in fila:
		atendidos.append(f)
	atendidos = ', '.join(atendidos)

	print('\nFCFS')
	print('     Ordem: ', atendidos)
	print('     Cilindros: ', cilindros)

def main():
	# fila_espera = []

	# Lendo arquivo
	try:
		if len(sys.argv) < 2:
			print ('arquivo não especificado')
			return
		else:
			arquivo = open(sys.argv[1])
			cabecote = arquivo.readline().replace('\n', '')	# Posição inicial do cabeçote
			tam_fila = arquivo.readline().replace('\n', '')	# Tamanho da fila de espera
			fila = arquivo.readline().split()		# Fila de espera
			arquivo.close()
	except FileNotFoundError:
		print("arquivo não encontrado")
		return

	FCFS(fila, cabecote)

if __name__ == '__main__':
		main()