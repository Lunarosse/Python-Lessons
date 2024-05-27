with open('C:\\Users\\aysegul\\Documents\\e.txt','r+')as dosya:
    icerik =dosya.read().upper()
    dosya.seek(0)
    dosya.write(icerik)