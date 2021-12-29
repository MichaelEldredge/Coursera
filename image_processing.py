from PIL import Image

im = Image.open("img_bronze_rgba.gif")
im.show()

im.convert('RGB').save('output.png')