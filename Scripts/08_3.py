with open('C:\\Users\\aysegul\\Documents\\e.txt','r+')as dosya:
    icerik = dosya.read()
    yeni_icerik=icerik.replace('elma','elmaa')
    dosya.seek(0)
    dosya.write(yeni_icerik)