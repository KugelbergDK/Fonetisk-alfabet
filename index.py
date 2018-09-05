#!/usr/bin/env python3

fonetisk = {
	"A": "Alfa",		"B": "Bravo",		"C": "Charlie",
	"D": "Delta",		"E": "Echo",		"F": "Foxtrot",
	"G": "Golf",		"H": "Hotel",		"I": "India",
	"J": "Juliett",		"K": "Kilo",		"L": "Lima",
	"M": "Mike",		"N": "November",	"O": "Oscar",
	"P": "Papa",		"Q": "Quebec",		"R": "Romeo",
	"S": "Sierra",		"T": "Tango",		"U": "Uniform",
	"V": "Victor",		"W": "Whiskey",		"X": "Xray",
	"Y": "Yankee",		"Z": "Zulu",		"Æ": "Ægir",
	"Ø": "Ødis",		"Å": "Åse",			"1": "1",
	"2": "2",			"3": "3",			"4": "4",
	"5": "5",			"6": "6",			"7": "7",
	"8": "8",			"9": "9",			"0": "0",
	".": "."
}

choice = ""
print ("Indtast 'QUIT' for at afslutte. \n")
while True:
	choice = input("Vælg bogstav: ").upper()
	if choice == "QUIT":
		break
	if len(choice) == 1:
		print (fonetisk[choice])
	if len(choice) >= 2:
		for letter in choice:
			print (fonetisk[letter] +  " ", end=' ')
		print ("\n")
	