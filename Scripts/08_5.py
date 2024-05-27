with open('C:\\Users\\aysegul\\Documents\\e.txt', 'r+') as dosya:
    icerik=dosya.read()
    dosya.seek(0)
    dosya.write('Sütun1,Sütun2,Sütun3\n'+icerik)