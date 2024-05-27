liste=("elma","armut","kiraz")
with open ("C:\\Users\\aysegul\\Documents\\e.txt","r+") as dosya:
    for eleman in liste:
        dosya.write(eleman+'\n')
    dosya.seek(0)
    okunan_liste=dosya.readlines()
    print(okunan_liste)