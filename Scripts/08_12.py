from PIL import image
try:
    img=Image.open('muffin.png')
    img.save('muffin.jpeg','JPEG')
except IOError:
    print('dosya işlemlerinde bir hata oluştu')
