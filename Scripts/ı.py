a=int(input())
toplam=0
while a!=0:
     if a<0:
       break
     toplam=toplam+a
     a=int(input())
else:
 print(toplam)