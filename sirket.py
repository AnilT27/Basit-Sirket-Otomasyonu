class Sirket():
    def __init__(self,ad):
        self.ad = ad
        self.calisma = True

    def program(self):
        secim = self.menuecim()
        if secim == 1:
            self.calisanekle()
        if secim == 2:
            self.calisancikar()
        if secim == 3:
            ay_yil_bazi = input("YILLIK BAZDA MI GÖRMEK İSTERSİNİZ?(e/h): ")
            if ay_yil_bazi == "e":
                self.verilecekmaaslar(hesap="y")
            else:
                self.verilecekmaaslar()
        if secim == 4:
            self.maaslariver()
        if secim == 5:
            self.masrafgir()
        if secim == 6:
            self.gelirgir()
        if secim == 7:
            self.calisangor()

    def menuecim(self):
        secim = int(input("""
        *** {} Otomosyona hoş geldiniz.***
        1-Çalışan Ekle
        2-Çalışan Çıkar
        3-Verilen Maaşları Göster
        4-Maaşları Ver
        5-Masraf Gir
        6-Gelir gir
        7-Çalışanları Göster
        Seçiminizi Giriniz:
        """.format(self.ad) ))
        while secim <1 or secim >7:
            secim = int(input("Lütfen 1-7 aralığında belirtilen değerlerden giriniz!"))

        return secim

    def calisanekle(self):
        id = 1
        ad = input("ÇALIŞANIN ADINI GİRİNİZ: ")
        soyad = input("ÇALIŞANIN SOYAD GİRİNİZ: ")
        maas = int(input("ÇALIŞANIN MAAŞ GİRİNİZ: "))
        cinsiyet = input("ÇALIŞANIN CİNSİYET GİRİNİZ: ")
        yas = int(input("ÇALIŞANIN YAŞ GİRİNİZ: "))

        with open("calisanlar.txt","r") as dosya:
            calisanlarlistesi = dosya.readlines()

        if len(calisanlarlistesi) == 0:
            id = 1
        else:
            with open("calisanlar.txt","r") as dosya:
                id = int(dosya.readlines()[-1].split(")")[0]) + 1

        with open("calisanlar.txt","a+") as dosya:
            dosya.write("{})-{}-{}-{}-{}-{}\n".format(id,ad,soyad,maas,cinsiyet,yas))

    def calisancikar(self):
        with open("calisanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()

        gCalisanlar = []

        for calisan in calisanlar:
            gCalisanlar.append(" ".join(calisan[:-1].split("-")))
        for calisan in gCalisanlar:
            print(calisan)
        secim = int(input("Lütfen 1-{} Arasında bir seçim yapın.".format(len(gCalisanlar))))
        while secim < 1 or secim > len(gCalisanlar):
            secim = int(input("LÜTFEN 1-{} ARALIĞINDA BİR DEĞER GİRİN.".format(len(gCalisanlar))))
        calisanlar.pop(secim - 1)
        sayac = 1
        dcalisanlar = []
        for calisan in calisanlar:
            dcalisanlar.append(str(sayac) + ")" + calisan.split(")")[1])
            sayac +=1
        with open("calisanlar.txt","w") as dosya:
            dosya.writelines(dcalisanlar)
    def verilecekmaaslar(self,hesap = "a"):
        """Hesap: a ise aylık , y ise yıllık hesap yapılır"""
        with open("calisanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()
        maaslar = []

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))
        if hesap == "y":
            print("BU YIL VERİELECEK TOPLAM MAAŞ: {}".format(sum(maaslar) * 12))
        else:
            print("BU AY VERİELECEK TOPLAM MAAŞ: {}".format(sum(maaslar)))

    def maaslariver(self):

        with open("calisanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()
        maaslar = []

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))

        toplamMaas = sum(maaslar)
        ### Butceden değer alma ###
        with open("butce.txt","r") as dosya:
            tbutce = int(dosya.readlines()[0])
        tbutce = tbutce - toplamMaas

        with open("butce.txt","w") as dosya:
            dosya.write(str(tbutce))

    def masrafgir(self):
        id = 1
        masrafisim = input("Masraf ismi girin: ")
        masraf = int(input("Ne kadar masraf yapıldı: "))

        with open("masraflar.txt","r") as dosya:
            masraflistesi = dosya.readlines()

        if len(masraflistesi) == 0:
            id = 1
        else:
            with open("masraflar.txt","a+") as dosya:
                id = int(dosya.readlines()[-1].split(")")[0]) + 1

        with open("masraflar.txt","a+") as dosya:
            dosya.write("{}){}-{}\n".format(id,masrafisim,masraf))
    def gelirgir(self):
        id = 1
        gelirisim = input("Gelir ismi girin: ")
        gelir = int(input("Ne kadar Gelir Geldi: "))

        with open("gelirler.txt","r") as dosya:
            gelirlistesi = dosya.readlines()

        if len(gelirlistesi) == 0:
            id = 1
        else:
            with open("gelirler.txt","r") as dosya:
                id = int(dosya.readlines()[-1].split(")")[0]) + 1

        with open("gelirler.txt","a+") as dosya:
            dosya.write("{}){}-{}\n".format(id,gelirisim,gelir))
    def calisangor(self):
        with open("calisanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()

        gCalisanlar = []

        for calisan in calisanlar:
            gCalisanlar.append(" ".join(calisan[:-1].split("-")))
        for calisan in gCalisanlar:
            print(calisan)
sirket = Sirket("Anıl Mekatronik")


while sirket.calisma:
    sirket.program()
