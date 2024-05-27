with open('C:\\Users\\aysegul\\Documents\\e.txt','r+') as dosya:
 satirlar = dosya.readlines()
 dosya.seek(0)
 for i,satir in enumerate(satirlar,1):
     dosya.write(f"{i}.{satir}")