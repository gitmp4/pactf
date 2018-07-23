# PACTF 2018: Truly Blue?
# Explanation:
# If you zoom in on some of the pixels in the image, they will appear to have slightly different shade of blue.
# I wrote a temporary program in Python to identify the colors that make up the image.
# I found most of the picture is of the RGB value (0, 49, 156) and the rest is (0,49,157), making it difficult
# to distinguish the two colors apart.

# (This image linked shows all the (0,49,157) pixels highlited in white https://imgur.com/gallery/guTIPmy)

# A common way of hiding images is using the least significant bit. 
# This program takes the least significant bits of each RGB value and each of them.
# If you take the output of the program and convert from binary to ASCII you should get this output:

# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut eleifend, metus accumsan accumsanpharetra,
# dui justo lobortis augue, non bibendum sapien lacus a nulla. Praesent non libero et magnaornare interdum.
# Vivamus et mi et justo tincidunt porttitor placerat in nisl. Nam mollis quam sitamet iaculis volutpat.
# Nulla posuere pulvinar est, ac consectetur ex rhoncus non. Vivamus efficitur,ex vel lobortis faucibus,
# massa neque iaculis libero, eu dictum orci odio ut ante. Phasellus luctusmagna vel euismod cursus.
# Donec et est rhoncus, lacinia metus in, sodales lectus. Sed posuere, nibhvitae egestas rutrum, nisl odio iaculis urna,
# et bibendum dolor augue tristique lacus. Ut nuncmetus, blandit a nisl vitae, pulvinar fringilla justo.
# The flag is "last bitsmatter". Congratulations! You cracked the code! ect...


from PIL import Image

# Opens Image
image = Image.open("true.png")
picture = image.load()

x = image.size[0]
y = image.size[1]
string = ""

# Goes through every pixel, finds its RGB value and then takes its least significant bit and adds it to the string
for g in range(0,128):
	for p in range(0,128):
		colors = picture[p,g]
		string = string + str(colors[0]%2) + str(colors[1]%2) + str(colors[2]%2)
	print(string)

