
def nadji_max_put(n,i):
	#racuna put do zadate pozicije na dnu piramide
	# na svakom spratu iznad postoje dva nacina da se spusti do zadate pozicije
	# osim ako je to pozicija na samoj ivici piramide, i u tom slucaju je jedan nacin

	sprat = piramida[n]

	if len(piramida[n]) == 1: 
		return sprat[0]


	elif i == 0 :

		suma = nadji_max_put(n-1,i) + sprat[i]
		return suma

	elif i+1 >= len(piramida[n]):

		suma = nadji_max_put(n-1, i-1) + sprat[-1]	
		return suma

	else:

		prvi = nadji_max_put(n-1,i) + sprat[i]
		sledeci = nadji_max_put(n-1,i+1) + sprat[i+1]

		return max(prvi,sledeci)

def sumiraj_me(piramida):

	n = len(piramida)
	maksimumi = []

	dno_piramide = piramida[n-1]

	for i in range(len(dno_piramide)-1):
		a = nadji_max_put(n-1,i)
		maksimumi.append(a)

	print "Najveca suma je: " , max(maksimumi)	
		
	
piramida = [[75],[95,64],[17,47,82],[18,35,87,10],[20,04,82,47,6],[19,1,23,75,03,34],[88,2,77,73,7,63,67],[99,65,4,28,06,16,70,92],[41,41,26,56,83,40,80,70,3],[41,48,72,33,47,32,37,16,94,29],[53,71,44,65,25,43,91,52,97,51,14],[70,11,33,28,77,73,17,78,39,68,17,57],[91,71,52,38,17,14,91,43,58,50,27,29,48],[63,66,04,68,89,53,67,30,73,16,69,87,40,31],[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23] ]

sumiraj_me(piramida)

#resenje je 930 za zadati primer

