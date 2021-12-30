from PIL import Image

im = Image.open("img_bronze_rgba.gif")

newim = im.convert('RGB')
newim.show()