import sys

print("-----Kullanıcı adı bilinmediği için bu bilgiyi veriyorum.-----")
print("Kullanıcı adı:aleyna kaya eğer yanlış girilirse program başlamaz.")
print("---PROGRAMIN BAŞLANGICI---")

 

i=0
kullanici='aleyna kaya'
while i<3:
    
    
    a=input("Lütfen kullanıcı adınızı giriniz:")
    
    if a==kullanici:
         print("--- WELCOME ---")
         i=3 
    else:
             i=i+1
             if i==3:
                 print("Please try again later..") 
                 sys.exit()
                 

                 
                 
dersler=[]
i=0
a=int(input("Kaç ders seçmek istersiniz:"))


while a<3 or a>5:

        print("You failed in class")
        a=int(input("Kaç ders seçmek istersiniz:"))
        


while i<a:
    ders=input("Derslerinizi seçiniz:")
    i=i+1
    dersler.append(ders)
    
print("DERSLERİNİZ:",dersler)
lesson=input("Bir ders seçiniz ve sınava giriniz:")
vize=int(input("Vize notunuzu giriniz:"))
final=int(input("Final notunuzu giriniz:"))
proje=int(input("Proje notunuzu giriniz:"))
sozluk={"vize":vize,"final":final,"proje":proje}
print("NOTLARINIZ:",sozluk)
ortalama=0
ortalama=(vize/100*30)+(final/100*50)+(proje/100*20)
print("Ortalamanız:",ortalama)

harf=''

if ortalama>=90:
    harf='AA'
elif ortalama>=70 and ortalama<90:
    harf='BB'
elif ortalama>=50 and ortalama<70:
    harf='CC'
elif ortalama<=30 and ortalama<50:
    harf='DD'
else:
    harf='FF'


    
print("Harf notunuz:",harf)