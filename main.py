import sys

# Algoritmo FCFS
def FCFS(fila):
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
	print('     Cilindros: ', cilindros, '\n')



# Algoritmo SSTF
def SSTF(fila):
	cilindros = 0
	cabeca = fila.pop(0)
	atendidos = [cabeca]
	SSTF_help(fila, cabeca, atendidos, cilindros)

def SSTF_help(fila, cabeca, atendidos, cilindros):
	if len(fila) == 0:
		atendidos = ', '.join(atendidos)

		print('SSTF')
		print('     Ordem: ', atendidos)
		print('     Cilindros: ', cilindros, '\n')
		return
	else:
		pos_menor = menor_diferenca(fila, cabeca)
		atendidos.append(fila[pos_menor])
		atual = fila.pop(pos_menor)

		c = abs(int(atual) - int(cabeca))
		cilindros += c

		SSTF_help(fila, atual, atendidos, cilindros)
		
def menor_diferenca(fila, cabeca):
	diff = []
	for f in fila:
		diff.append(abs(int(f) - int(cabeca))) 
	menor = min(diff)
	return diff.index(menor)





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
			fila.insert(0, cabecote)
			arquivo.close()
	except FileNotFoundError:
		print("arquivo não encontrado")
		return

	FCFS(fila)
	SSTF(fila)

if __name__ == '__main__':
		main()