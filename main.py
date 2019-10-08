from PIL import Image
from modules import pixelimage, pixel

image = Image.open('test4.jpg', 'r')

test = pixelimage.PixelImage(image)