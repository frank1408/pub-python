#!/usr/bin/python3
# CREADO POR FRANKLIN RODRIGUEZ

import random

abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

international_dictionary = {
'a': "alpha",
'b': "bravo",
'c': "charlie",
'd': "delta",
'e': "echo",
'f': "foxtrot",
'g': "golf",
'h': "hotel",
'i': "india",
'j': "juliet",
'k': "kilo",
'l': "lima",
'm': "mike",
'n': "november",
'o': "oscar",
'p': "papa",
'q': "quebec",
'r': "romeo",
's': "sierra",
't': "tango",
'u': "uniform",
'v': "victor",
'w': "whisky",
'x': "x-ray",
'y': "yankee",
'z': "zulu"
} # international_dictionary

def getList( dictionary ):
	x = []
	for i in dictionary:
		x.append( dictionary[i] )
	return x

def showmethetruth(mydictionary, letter):
	return mydictionary[letter];

def comprobar( mydictionary, word ):
	return mydictionary[word[0]] == word

def refuerzoPositivo():
	good_phrase = ["Very Good", "Fine", "You Did It","Excellent"]
	ans = random.randint(0, (len(good_phrase)-1) );
	print("\t",good_phrase[ans] )
	
def mis_resultados():
	print("\nCorrectas ",aciertos)
	print("Errores ",errores)

def clear_screen():
	print("\n" * 255)


buenas = set()
aciertos = 0
errores = 0
anterior = ""
res = ""
iteraciones = 1
total = getList(international_dictionary)

print("""
Alfabeto De Deletreo Para Radiotelefonia,
Utilizado Internacionalmente Por (OACI/ICAO) 

Responde Cual Es La Palabra Que
Esta Asociada a La Letra.

Si Quieres Salir Escribe Exit
""")
input()
clear_screen()

while len(buenas) < 26 and errores < 9:
	iteraciones+=1
	num_random = random.randint(0,25)
	letter_random = abc[num_random];
	res = ""
	# buenas vs total, letter_random = letra_faltante
	if len(buenas) > 9:
		buenass = list(buenas)  # llevo
		faltan = [] # lo que falta
		for element in total:
			if element not in buenass:
				faltan.append(element)
		word_left = faltan[0]
		letter_random = word_left[0]
		#for i in faltan:
			#print(i[0])
	# buenas vs total, letter_random = letra_faltante

	anterior = letter_random

	try:
		answer = input( "\n\nPalabra Con "+ letter_random + " ?\t\t")
		answer = str(answer)
		answer = answer.lower()
		if len(answer) < 2:
			print("\tLa respuesta correcta es: ", international_dictionary[letter_random], "\n" )
			errores+=1

		if answer == "exit":
			break
		res = comprobar( international_dictionary, answer )
		if res == True:
			refuerzoPositivo();
			buenas.add(answer)
			aciertos+=1
		else:
			print("\tLa respuesta correcta es: ", international_dictionary[letter_random], "\n" )
			errores+=1
	except:
		pass

mis_resultados()
if len(buenas) == 25:
	print("Felicitaciones ya sabes las 26 letras")
print('Sigue Aprendiendo, Vuelve Pronto,Con El Tiempo Se Olvida')

