import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor
from PIL import ImageChops
import os

def genPic1(spe, col, prt, anname):
	backdrop = Image.open("parts/backdrop.png")
	body = Image.open("parts/" + spe + "/basecolor.png")
	lines = Image.open("parts/" + spe + "/lines.png")
	spots = Image.open("parts/" + spe + "/spots.png")
	rings = Image.open("parts/" + spe + "/rings.png")
	stripes = Image.open("parts/" + spe + "/stripes.png")

	tmp = Image.new('RGBA', spots.size, (0,0,0,0))
	draw = ImageDraw.Draw(tmp)
	draw.rectangle(((0, 0), spots.size), fill=(col))

	tmp2 = Image.new('RGBA', spots.size, (0,0,0,1))
	draw = ImageDraw.Draw(tmp2)
	draw.rectangle(((0, 0), spots.size), fill=(col))

	body2 = ImageChops.multiply(body, tmp2)

	Image.alpha_composite(backdrop, body2).save("BIRDS/test2.png")
	test2 = Image.open("BIRDS/test2.png")

	if prt == "-ringed":
		rings2 = ImageChops.multiply(rings, tmp)
		Image.alpha_composite(test2, rings2).save("BIRDS/test3.png")
	elif prt == "-spotted":
		spots2 = ImageChops.multiply(spots, tmp)
		Image.alpha_composite(test2, spots2).save("BIRDS/test3.png")
	elif prt == "-striped":
		stripes2 = ImageChops.multiply(stripes, tmp)
		Image.alpha_composite(test2, stripes2).save("BIRDS/test3.png")
	else:
		Image.alpha_composite(test2, lines).save("BIRDS/test3.png")
	
	test3 = Image.open("BIRDS/test3.png")
	Image.alpha_composite(test3, lines).save("BIRDS/" + str(anname + ".png"))
	#os.remove("BIRDS/test2.png")
	#os.remove("BIRDS/test3.png")
	#imeg = Image.open("BIRDS/" + str(anname + ".png"))
	#imeg.show()
		
def genPic2(spe, col, prt, annameONE):
	backdrop = Image.open("parts/backdrop.png")
	body = Image.open("parts/" + spe + "/basecolor.png")
	lines = Image.open("parts/" + spe + "/lines.png")
	spots = Image.open("parts/" + spe + "/spots.png")
	rings = Image.open("parts/" + spe + "/rings.png")
	stripes = Image.open("parts/" + spe + "/stripes.png")

	tmp = Image.new('RGBA', spots.size, (0,0,0,0))
	draw = ImageDraw.Draw(tmp)
	draw.rectangle(((0, 0), spots.size), fill=(col))

	tmp2 = Image.new('RGBA', spots.size, (0,0,0,1))
	draw = ImageDraw.Draw(tmp2)
	draw.rectangle(((0, 0), spots.size), fill=(col))

	body2 = ImageChops.multiply(body, tmp2)

	Image.alpha_composite(backdrop, body2).save("BIRDS/test2.png")
	test2 = Image.open("BIRDS/test2.png")

	if prt == "-ringed":
		rings2 = ImageChops.multiply(rings, tmp)
		Image.alpha_composite(test2, rings2).save("BIRDS/test3.png")
	elif prt == "-spotted":
		spots2 = ImageChops.multiply(spots, tmp)
		Image.alpha_composite(test2, spots2).save("BIRDS/test3.png")
	elif prt == "-striped":
		stripes2 = ImageChops.multiply(stripes, tmp)
		Image.alpha_composite(test2, stripes2).save("BIRDS/test3.png")
	else:
		Image.alpha_composite(test2, lines).save("BIRDS/test3.png")
	
	test3 = Image.open("BIRDS/test3.png")
	Image.alpha_composite(test3, lines).save("BIRDS/" + str(annameONE + ".png"))
	#os.remove("BIRDS/test2.png")
	#os.remove("BIRDS/test3.png")
	#imeg = Image.open("BIRDS/" + str(annameONE + ".png"))
	#imeg.show()
