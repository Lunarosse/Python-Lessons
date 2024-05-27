from PIL import Image
try:
    img=Image.open('muffin.jpg')
    img.show()
except FileNotFoundError:
    print("Image not found")
except I0Error:
    print("Image not opened")
