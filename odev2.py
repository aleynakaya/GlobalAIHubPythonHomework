mylist=[]
ad=input("Adınızı giriniz:")
soyad=input("Soyadınızı giriniz:")
yas=int(input("Yaşınızı giriniz:"))
dTarih=int(input("Doğum yılınızı giriniz:"))
print("------BİLGİLER------")
mylist.append(ad)
mylist.append(soyad)
mylist.append(yas)
mylist.append(dTarih)
for i in range(4):
    print(mylist[i])
    
if yas<18 : 
    print("Çıkamazsınız çünkü çok tehlikeli.")
else:
    print("Caddeye çıkabilirsin.")





