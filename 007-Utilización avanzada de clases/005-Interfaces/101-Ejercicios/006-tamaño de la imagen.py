from PIL import Image

imagen = Image.open("josevicente.jpg")

anchura,altura = imagen.size		# Cojo altura y anchura

for x in range(0,anchura):
  for y in range(0,altura):
		pixel = imagen.getpixel((x, y))
		print(pixel1)
