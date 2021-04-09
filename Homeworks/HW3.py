a=0
kullanıcıadı=input("KULLANICI ADINIZI GİRİNİZ : ")
if(kullanıcıadı=="my"):
    while True:
        pword=input("ŞİFRENİZİ GİRİNİZ : ")
        if(pword=="123456"):
            print("SİSTEME GİRDİNİZ.")
            break
        else:
            print("ŞİFRENİZİ YANLIŞ GİRDİNİZ")
            a+=1
            if(a==3):
                print("3 KERE YANLIŞ GİRİŞ YAPTINIZ.\nBİR SÜRE SONRA TEKRAR DENEYİNİZ")
                break
            continue
else:
    print("SİSTEMDE KAYDINIZ BULUNMAMAKTADIR")
    print("SİSTEME KAYIT YAPTIRABİLİRSİNİZ")
