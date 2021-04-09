sayi1=int(input("LÜTFEN TEK BASAMAKLI BİR SAYI GİRİNİZ : "))
while (0>sayi1 or sayi1>=10) :
    print("GİRDİĞİNİZ SAYI TEK BASAMAKLI OLMALIDIR.")
    sayi1=int(input("LÜTFEN TEK BASAMAKLI BİR SAYI GİRİNİZ : "))
for i in range(0,sayi1+1,2):
    print(i,end=" ")


