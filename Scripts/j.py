from random import randint
print('0 ile programdan çıkabilirsiniz!')
a=int(input())
rastgele=randint(1,76)
say=1
while not(a==0 or a == rastgele):
    if a>rastgele:
        print('Daha küçük sayı giriniz')
    else:
        print('Daha büyük sayı giriniz')
    say+=1
    a=int(input())
if a!=0:
    print(say,'Defada buldunuz!')