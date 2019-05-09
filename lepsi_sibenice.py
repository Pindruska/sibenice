"""
1. vylosuj slovo
2. vypiš pole
3. zeptej se na písmeno
4. hledej pismeno ve slově
	4a. pokud je písmeno ve slově, místo - napiš písmeno
	4b. pokud není písmeno ve slově, zvyš level +1, vypiš obrázek
5. zkontroluj stav hry:
	5a. hráč vyhrál, pokud v poli nejsou '-' a level <=8
		pogratuluj
	5b. hráč prohrál, pokud level >8
		informuj ho, že prohrál

3-5 opakuj dokud hráč nevyhraje nebo neprohraje

"""
from random import choice
from obrazek_sibenice import obrazek #z Gitsu jsem si stahla kod s obrazky sibenice

pismena = ["Ě", "Š", "Č", "Ů", "Ž", "Ý", "Á", "Í", "É", "Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "Ú", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ů", "Y", "X", "C", "V", "B", "N", "M"]
seznam_slov = [
				"stromek", "trávník", "krabice", "jahody", "stavení"
				"čokoláda", "marmeláda", "baterka", "čudlík"
				]

def vyber_slovo(seznam_slov):
	"""ze seznamu slov vybere jedno slovo, prevede ho na velka pismena a vrati"""
	seznam_pouzitych_slov = []
	slovo = choice(seznam_slov)
	while True:
		if slovo not in seznam_pouzitych_slov:
			seznam_pouzitych_slov.append(slovo)
			return slovo.upper()
		else:
			slovo = choice(seznam_slov)

def zamen(pole, pozice, pismeno):
	"""zameni podtrzitko v poli na zadane pozici za zadane pismeno"""
	zacatek = pole[ :pozice]
	prostredek = pismeno
	konec = pole[pozice+1: ]
	return zacatek + prostredek + konec

def najdi_pismena(slovo, hledane_pismeno):
	"""prohleda slovo pismeno po pismenu
	a vrati vsechny pozice, ve kterych se 
	pismeno vyskytuje"""
	seznam_pozic = []
	pozice = 0
	for pismeno in slovo:
		if pismeno == hledane_pismeno:
			pozice = slovo.index(pismeno, pozice)
			seznam_pozic.append(pozice)
			pozice +=1
		else:
			pozice +=1
	return seznam_pozic

def zjisti_odpoved_ano_nebo_ne(otazka):
	"""Zeptá se na otázku a vrátí True nebo False podle odpovědi (ano/ne)"""
	while True: #tak se rekne v Pythonu "pořád dokola" ;-)
		odpoved = (input(otazka)).lower()
		if odpoved == "ano" or odpoved == "a":
			return True
		elif odpoved == "ne" or odpoved == "n":
			return False
		else:
			print("Nerozumím. Odpovídej ano nebo ne.")

def sibenice():
	slovo = vyber_slovo(seznam_slov)
	pole = "_" * len(slovo)
	level = 0

	print(pole)

	while True:
		pismeno = (input("Napiš písmeno: ")).upper()
		if pismeno not in pismena:
			print(f"{pismeno} není písmeno!")
		else:
			if pismeno in slovo:
				if slovo.count(pismeno) == 1:
					pole = zamen(pole, slovo.index(pismeno), pismeno)
					print(pole)
				else:
					seznam_pozic = najdi_pismena(slovo, pismeno)
					for pozice in seznam_pozic:
						pole = zamen(pole, pozice, pismeno)
					print(pole)
			else:
				print("Zadané písmeno není ve slově.")
				level += 1
				print(obrazek(level))
				if level >8:
					print(f"Prohrál/a jsi! Hledané slovo byl {slovo}")
					break
				else:
					print(pole)


		if "_" not in pole:
			print("Gratuluji, vyhrál/a jsi!")
			break

while True:
	sibenice()
	if zjisti_odpoved_ano_nebo_ne("Chceš si zahrát znovu? "):
		sibenice()
	else:
		break

