with open('C:\\Users\\aysegul\\Documents\\e.txt', 'r+') as dosya:
    icerik=dosya.read()
    ters_icerik=icerik[::-1]
    dosya.seek(0)
    dosya.write(ters_icerik)