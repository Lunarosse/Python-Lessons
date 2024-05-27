from datetime import datetime
bugun= datetime.today().strftime('%Y-%m-%Y')
with open('C:\\Users\\aysegul\\Documents\\e.txt','r+') as dosya:
    satirlar=dosya.readlines()
    dosya.seek(0)
    dosya.writelines([f"{bugün}{satir}"for satir in satirlar])
    dosya.truncate()