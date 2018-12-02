import sys

# Algoritmo FCFS
def FCFS(fila):
	fila_espera = fila[:]
	atendidos = []
	cilindros = 0

	for i in range(len(fila_espera) - 1):
		c = max(int(fila_espera[i]), int(fila_espera[i+1])) - min(int(fila_espera[i]), int(fila_espera[i+1]))
		cilindros += c

	for f in fila_espera:
		atendidos.append(f)
	atendidos = ', '.join(atendidos)

	print('\nFCFS')
	print('     Ordem: ', atendidos)
	print('     Cilindros: ', cilindros, '\n')



# Algoritmo SSTF
def SSTF(fila):
	fila_espera = fila[:]
	cilindros = 0
	cabeca = fila_espera.pop(0)
	atendidos = [cabeca]
	SSTF_help(fila_espera, cabeca, atendidos, cilindros)

def SSTF_help(fila_espera, cabeca, atendidos, cilindros):
	diff = []
	if len(fila_espera) == 0:
		atendidos = ', '.join(atendidos)

		print('SSTF')
		print('     Ordem: ', atendidos)
		print('     Cilindros: ', cilindros, '\n')
		return
	else:
		menor = min(menor_diferenca(fila_espera, cabeca, diff))
		pos_menor = diff.index(menor)
		atendidos.append(fila_espera[pos_menor])
		atual = fila_espera.pop(pos_menor)

		c = abs(int(atual) - int(cabeca))
		cilindros += c

		SSTF_help(fila_espera, atual, atendidos, cilindros)
		
def menor_diferenca(fila_espera, cabeca, diff):
	for f in fila_espera:
		diff.append(abs(int(f) - int(cabeca))) 
	return diff 


# Algoritmo SCAN Sobe
def SCAN_sobe(fila):
	fila_espera = fila[:]
	cilindros = 0
	cabeca = fila_espera.pop(0)
	atendidos = [int(cabeca)]

	for i in range(len(fila_espera)):
		fila_espera[i] = int(fila_espera[i])

	SCAN_sobe_help(fila_espera, cabeca, atendidos, cilindros)

def SCAN_sobe_help(fila_espera, cabeca, atendidos, cilindros):
	diff = []
	menores = []
	maiores = []

	for f in fila_espera:
		if f < int(cabeca):
			menores.append(f)

		elif f > int(cabeca):
			maiores.append(f)
	
	while len(menores) > 0:
		m = max(menores)
		atendidos.append(m)
		fila_espera.pop(fila_espera.index(m))
		menores.pop(menores.index(m))

	while len(maiores) > 0:
		m = min(maiores)
		atendidos.append(m)
		fila_espera.pop(fila_espera.index(m))
		maiores.pop(maiores.index(m))

	for i in range(len(atendidos) - 1):
		c = abs(atendidos[i + 1] - atendidos[i])
		cilindros += c

	for i in range(len(atendidos)):
		atendidos[i] = str(atendidos[i])

	atendidos = ', '.join(atendidos)
	print('SCAN sobe')
	print('     Ordem: ', atendidos)
	print('     Cilindros: ', cilindros, '\n')
	
	# print('menores', menores)
	# print('maiores', maiores)
	# print('atendidos', atendidos)
	# print('fila', fila_espera)



def main():
	try:
		if len(sys.argv) < 2:
			return print ('arquivo não especificado')
		else:
			arquivo = open(sys.argv[1])
			cabecote = arquivo.readline().replace('\n', '')	# Posição inicial do cabeçote
			tam_fila = arquivo.readline().replace('\n', '')	# Tamanho da fila de espera
			fila = arquivo.readline().split()		# Fila de espera
			fila.insert(0, cabecote)
			arquivo.close()

			for f in fila:
				if int(f) < 0 or int(f) > 199:
					return print("os setores requisitados devem variar entre 0 e 199")

	except FileNotFoundError:
		return print("arquivo não encontrado")

	FCFS(fila)
	SSTF(fila)
	SCAN_sobe(fila)

if __name__ == '__main__':
		main()