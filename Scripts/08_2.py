with open    (sayac.txt, 'r+') as dosya:
    deger=int(dosya.read())
    deger +=1
    dosya.seek(0)
    dosya.write(str(deger))