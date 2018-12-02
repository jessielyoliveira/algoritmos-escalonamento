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
	imprimir('\nFCFS', atendidos, cilindros)

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
		imprimir('SSTF', atendidos, cilindros)

		return
	else:
		menor = min(menor_diferenca(fila_espera, cabeca, diff))
		pos_menor = diff.index(menor)
		atendidos.append(fila_espera[pos_menor])
		atual = fila_espera.pop(pos_menor)

		c = abs(int(atual) - int(cabeca))
		cilindros += c

		SSTF_help(fila_espera, atual, atendidos, cilindros)
		


# Algoritmo SCAN Sobe
def SCAN_sobe(fila):
	fila_espera = fila[:]
	cabeca = fila_espera.pop(0)
	atendidos = [int(cabeca)]

	for i in range(len(fila_espera)):
		fila_espera[i] = int(fila_espera[i])

	SCAN_sobe_help(fila_espera, cabeca, atendidos)

def SCAN_sobe_help(fila_espera, cabeca, atendidos):
	diff = []
	cilindros = 0
	menores = []
	maiores = []

	for f in fila_espera:
		if f < int(cabeca):
			menores.append(f)

		elif f > int(cabeca):
			maiores.append(f)
	
	percorrer_menores(menores, atendidos, fila_espera)
	percorrer_maiores(maiores, atendidos, fila_espera)

	for i in range(len(atendidos) - 1):
		c = abs(atendidos[i + 1] - atendidos[i])
		cilindros += c

	for i in range(len(atendidos)):
		atendidos[i] = str(atendidos[i])

	atendidos = ', '.join(atendidos)
	imprimir('SCAN sobe', atendidos, cilindros)

# Algoritmo SCAN Desce
def SCAN_desce(fila):
	fila_espera = fila[:]
	cabeca = fila_espera.pop(0)
	atendidos = [int(cabeca)]

	for i in range(len(fila_espera)):
		fila_espera[i] = int(fila_espera[i])

	SCAN_desce_help(fila_espera, cabeca, atendidos)

def SCAN_desce_help(fila_espera, cabeca, atendidos):
	diff = []
	cilindros = 0
	menores = []
	maiores = []

	for f in fila_espera:
		if f < int(cabeca):
			menores.append(f)

		elif f > int(cabeca):
			maiores.append(f)
	
	percorrer_maiores(maiores, atendidos, fila_espera)
	percorrer_menores(menores, atendidos, fila_espera)

	for i in range(len(atendidos) - 1):
		c = abs(atendidos[i + 1] - atendidos[i])
		cilindros += c

	for i in range(len(atendidos)):
		atendidos[i] = str(atendidos[i])

	atendidos = ', '.join(atendidos)
	imprimir('SCAN desce', atendidos, cilindros)

# Funções auxiliares
def menor_diferenca(fila_espera, cabeca, diff):
	for f in fila_espera:
		diff.append(abs(int(f) - int(cabeca))) 
	return diff 

def percorrer_menores(menores, atendidos, fila_espera):
	while len(menores) > 0:
		m = max(menores)
		atendidos.append(m)
		fila_espera.pop(fila_espera.index(m))
		menores.pop(menores.index(m))

def percorrer_maiores(maiores, atendidos, fila_espera):
	while len(maiores) > 0:
		m = min(maiores)
		atendidos.append(m)
		fila_espera.pop(fila_espera.index(m))
		maiores.pop(maiores.index(m))

def imprimir(algoritmo, atendidos, cilindros):
	print(algoritmo)
	print('     Ordem: ', atendidos)
	print('     Cilindros: ', cilindros, '\n')


# Função principal
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
	SCAN_desce(fila)

if __name__ == '__main__':
		main()