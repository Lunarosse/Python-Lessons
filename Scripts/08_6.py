with open('C:\\Users\\aysegul\\Documents\\e.txt,'r+') as dosya:
    satirlar=dosya.readlines()
    dosya.seek(0)
    dosya.writelines(satir for satir in satirlar if 'Sütun3'not in satir)
    dosya.truncate()