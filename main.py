def toplama(x,y):
    return x + y

def çıkarma(x,y):
    return x - y

def çarpma(x,y):
    return x * y

def bölme(x,y):
    return x / y

def üs(x,y):
    return x ** y

islemler = {
    "1": toplama,
    "2": çıkarma,
    "3": çarpma,
    "4": bölme,
    "5": üs
}

def menü():
    while(True):
        print("Menü".center(50,"*"))
        print("1-Toplama")
        print("2-Çıkarma")
        print("3-Çarpma")
        print("4-Bölme")
        print("5-Üs Alma")
        print("0-Çıkış")

        islem = input("Hangi işlemi yapmak istiyorsunuz? ")

        if islem == "0":
            print("Çıkış yapılıyor...")
            break
        elif islem not in islemler:
            print("Geçersiz işlem! Lütfen 1-5 arasında bir seçim yapın.")
            continue

        try:
            x = int(input("Birinci sayıyı giriniz: "))
            y = int(input("İkinci sayiyi giriniz: "))
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz!")
            continue

        if islem == "4" and y == 0:
            print("Hata! 0'a bölünemez.")
            continue

        sonuc = islemler[islem](x,y)
        print("Sonuç:", sonuc)

menü()