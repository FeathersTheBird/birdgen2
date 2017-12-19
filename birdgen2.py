import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor
from PIL import ImageChops
import os
import picmaker as picmaker
from picmaker import *

os.system("title BirdGen 3000")

def main():

	
	f = open('birdgen.txt','a')
	
	colors = [
		"White",
		"Red",
		"Crimson",
		"Mistyrose",
		"Pink",
		"Orange",
		"Yellow",
		"Gold",
		"Green",
		"Olive",
		"Teal",
		"Blue",
		"Aqua",
		"Steelblue",
		"Indigo",
		"Violet",
		"Maroon",
		"Brown",
		"Sienna"
	]
	
	parts = [
		#"-capped",
		#"-beaked",
		#"-cheeked",
		#"-breasted",
		#"-footed",
		#"-eyed",
		#"-tailed",
		#"-winged",
		#"-crested",
		"-ringed",
		"-striped",
		"-spotted"
	]
		
	species = [
		"Hawk",
		"Eagle",
		"Duck",
		"Conure",
		"Dove",
		"Ibis",
		"Owl",
		"Finch",
		"Swallow",
		"Robin"
	]
	
	names = [
		"Jane",
		"Marie",
		"Nova",
		"Hal",
		"Ash",
		"Hayley",
		"Harrison Ford",
		"Disney",
		"Katie",
		"Mario & Luigi",
		"Michelle",
		"Johnny",
		"Cagney",
		"Bon Bon",
		"Chief",
		"Sam",
		"Woody",
		"Cliff",
		"Norm",
		"Carla",
		"Diane",
		"Charlie",
		"Chell",
		"Rita",
		"Scrooge",
		"Mickey",
		"Minnie",
		"Donald",
		"Daisy",
		"Horace",
		"Oswald"		
	]
	
	options = [
	"FOR CREATE-A-BIRD, PRESS 0.",
	"TO GENERATE NEW BIRDS, PRESS 1.",
	"FOR SPECIAL BIRDS, PRESS 2.",
	"TO QUIT, PRESS 3."
	]
	
	specials = [
	"thoths special boy"
	]
	
	spe = random.choice(species)
	col = random.choice(colors)
	prt = random.choice(parts)
	nme = random.choice(names)
	
	chance = (random.randint(1,100))
	if chance <= 1:
		spe = "Furby"
	
	annameONE = str(col + prt + " " + spe)
		

	def makeBird(colors, parts, species):
		for i in range(1,10):
			stringA = ((random.choice(colors)) + (random.choice(parts)) + " " + (random.choice(species)))
			print(stringA)
			f.write(str("- " + stringA + '\n'))
			
	def nameBird(names, colors, species):
		f.write('\n')
		for i in range(1,10):
			stringB = ((random.choice(names)) + "'s " + (random.choice(colors)) + " " + (random.choice(species)))
			print(stringB)
			f.write(str("- " + stringB + '\n'))	
		f.write('\n')
	
	def printBird():
		print(" ")
		print("---> CHECK OUT THESE SWEET NEW BIRDS!!! <---")
		makeBird(colors, parts, species)
		print(" ")
		print("---> CHECK OUT THESE OTHER AND EQUALLY SWEET NEW BIRDS!!! <---")
		nameBird(names, colors, species)
		print(" ")
		print("Pictured: " + annameONE)
		picmaker.genPic2(spe, col, prt, annameONE)
		imeg = Image.open("BIRDS/" + str(annameONE + ".png"))
		imeg.show()
		print(" ")
		#printOptions()
		
	def birdSpeOptions():
		print(" ")
		print("PICK A BIRD:")
		print(species[0] + ": 0")
		print(species[1] + ": 1")
		print(species[2] + ": 2")
		print(species[3] + ": 3")
		print(species[4] + ": 4")
		print(species[5] + ": 5")
		print(species[6] + ": 6")
		print(species[7] + ": 7")
		print(species[8] + ": 8")
		print(species[9] + ": 9")
		return input("TYPE THE NUMBER TO SELECT: ")
		
	def birdColOptions():
		print(" ")
		print(colors[0] + ": 0")
		print(colors[1] + ": 1")
		print(colors[2] + ": 2")
		print(colors[3] + ": 3")
		print(colors[4] + ": 4")
		print(colors[5] + ": 5")
		print(colors[6] + ": 6")
		print(colors[7] + ": 7")
		print(colors[8] + ": 8")
		print(colors[9] + ": 9")
		print(colors[10] + ": 10")
		print(colors[11] + ": 11")
		print(colors[12] + ": 12")
		print(colors[13] + ": 13")	
		print(colors[14] + ": 14")
		print(colors[15] + ": 15")
		print(colors[16] + ": 16")
		print(colors[17] + ": 17")
		print(colors[18] + ": 18")
		return input("TYPE THE NUMBER TO SELECT: ")
		
	def birdPartOptions():
		print(" ")
		print(parts[0] + ": 0")
		print(parts[1] + ": 1")
		print(parts[2] + ": 2")
		return input("TYPE THE NUMBER TO SELECT: ")
	
	def specialBoys():
		specialBird = random.choice(specials)
		print(" ")
		print("Pictured: " + specialBird)
		SB = Image.open("SB/" + specialBird + ".png")
		SB.show()
		
	def birdSpore():
		BIRDSPE = int(birdSpeOptions())
		if BIRDSPE == 0:
			spe = (species[0])
			print("You have selected " + spe + ".")
		elif BIRDSPE == 1:
			spe = (species[1])
			print("You have selected " + spe + ".")
		elif BIRDSPE == 2:
			spe = (species[2])
			print("You have selected " + spe + ".")
		elif BIRDSPE == 3:
			spe = (species[3])
			print("You have selected " + spe + ".")
		elif BIRDSPE == 4:
			spe = (species[4])
			print("You have selected " + spe + ".")
		elif BIRDSPE == 5:
			spe = (species[5])
			print("You have selected " + spe + ".")
		elif BIRDSPE == 6:
			spe = (species[6])
			print("You have selected " + spe + ".")
		elif BIRDSPE == 7:
			spe = (species[7])
			print("You have selected " + spe + ".")
		elif BIRDSPE == 8:
			spe = (species[8])
			print("You have selected " + spe + ".")
		elif BIRDSPE == 9:
			spe = (species[9])
			print("You have selected " + spe + ".")
		else:
			return input("Pick a valid species, please. ")
		BIRDCOL = int(birdColOptions())
		if BIRDCOL == 0:
			col = (colors[0])
			print("You have selected " + col + ".")
		elif BIRDCOL == 1:
			col = (colors[1])
			print("You have selected " + col + ".")
		elif BIRDCOL == 2:
			col = (colors[2])
			print("You have selected " + col + ".")
		elif BIRDCOL == 3:
			col = (colors[3])
			print("You have selected " + col + ".")
		elif BIRDCOL == 4:
			col = (colors[4])
			print("You have selected " + col + ".")
		elif BIRDCOL == 5:
			col = (colors[5])
			print("You have selected " + col + ".")
		elif BIRDCOL == 6:
			col = (colors[6])
			print("You have selected " + col + ".")
		elif BIRDCOL == 7:
			col = (colors[7])
			print("You have selected " + col + ".")
		elif BIRDCOL == 8:
			col = (colors[8])
			print("You have selected " + col + ".")
		elif BIRDCOL == 9:
			col = (colors[9])
			print("You have selected " + col + ".")
		elif BIRDCOL == 10:
			col = (colors[10])
			print("You have selected " + col + ".")
		elif BIRDCOL == 11:
			col = (colors[11])
			print("You have selected " + col + ".")
		elif BIRDCOL == 12:
			col = (colors[12])
			print("You have selected " + col + ".")
		elif BIRDCOL == 13:
			col = (colors[13])
			print("You have selected " + col + ".")
		elif BIRDCOL == 14:
			col = (colors[14])
			print("You have selected " + col + ".")
		elif BIRDCOL == 15:
			col = (colors[15])
			print("You have selected " + col + ".")
		elif BIRDCOL == 16:
			col = (colors[16])
			print("You have selected " + col + ".")
		elif BIRDCOL == 17:
			col = (colors[17])
			print("You have selected " + col + ".")
		elif BIRDCOL == 18:
			col = (colors[18])
			print("You have selected " + col + ".")
		else:
			return input("Pick a valid color, please. ")
		BIRDPART = int(birdPartOptions())
		if BIRDPART == 0:
			prt = (parts[0])
			print("You have selected " + prt + ".")
		elif BIRDPART == 1:
			prt = (parts[1])
			print("You have selected " + prt + ".")
		elif BIRDPART == 2:
			prt = (parts[2])
			print("You have selected " + prt + ".")
		else:
			return input("Pick a valid pattern, please. ")
		
		USERNAME = input("Enter your name, please. ")
		nme = str(USERNAME + "'s")
		
		anname = str(nme + " " + col + prt + " " + spe)
		
		print("Congrats! You have created the " + anname + "!" )
		picmaker.genPic1(spe, col, prt, anname)
		imeg = Image.open("BIRDS/" + str(anname + ".png"))
		imeg.show()
		
	def endGame():
		os._exit(0)
	
	#funky fresh#
	
	def printOptions():
		print("=== PICK AN ACTIVITY! ===")
		print(" ")
		print(options[0])
		print(options[1])
		print(options[2])
		print(options[3])
		print(" ")
		return input("Type selection and hit enter for birdy fun! ")
	
	selection = int(printOptions())
	if selection == 0:
		birdSpore()
	elif selection == 1:
		printBird()
	elif selection == 2:
		specialBoys()
	elif selection == 3:
		endGame()
	else:
		return input("Try again. ")
	
	f.close()
	
main()
