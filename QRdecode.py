from pyzbar.pyzbar import decode
from PIL import Image

path = input("Please enter a file path: ")

img = Image.open(path)

result = decode(img)
print(result)
