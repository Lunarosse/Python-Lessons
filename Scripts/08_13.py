from PIL import Image
try:
    img=Image.open('muffin.jpg')
    dondurulmus_img=img.rotate(90)
    dondurulmus_img.save('dondurulmus_muffin.jpg')
except IOError:
    print("It's impossible to save the image")