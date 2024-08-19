import random

p_kullanici_skor = 0
p_bilgisayar_skor = 0

def kullanici_secimi():
    while True:
        v_kullanici_girisi = input("'Taş, kağıt, makas' birini yazın: ").strip().lower()
        if v_kullanici_girisi in ["taş", "kağıt", "makas"]:
            return v_kullanici_girisi
        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")

def bilgisayar_secimi():
    return random.choice(["taş", "kağıt", "makas"])

def kim_kazandi(p_kullanici_secimi, p_bilgisayar_secimi):
    global p_kullanici_skor
    global p_bilgisayar_skor

    if p_kullanici_secimi == p_bilgisayar_secimi:
        return "Beraberlik!"
    elif (p_kullanici_secimi == "taş" and p_bilgisayar_secimi == "makas"):
        p_kullanici_skor += 1
        return "Kazandınız!"
    elif (p_kullanici_secimi == "kağıt" and p_bilgisayar_secimi == "taş"):
        p_kullanici_skor += 1
        return "Kazandınız!"
    elif (p_kullanici_secimi == "makas" and p_bilgisayar_secimi == "kağıt"):
        p_kullanici_skor += 1
        return "Kazandınız!"
    else:
        p_bilgisayar_skor += 1
        return "Kaybettiniz!"

def tekrar_oyna():
    while True:
        v_tekrar_oyna = input("Yeniden oynamak ister misiniz? (evet/hayır): ").strip().lower()
        print("==========================================")
        if v_tekrar_oyna in ["evet", "hayır"]:
            return v_tekrar_oyna
        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")

def tas_kagit_makas_oyna():
    global p_kullanici_skor
    global p_bilgisayar_skor

    v_oyuncu = input("Lütfen oyuncunun adını giriniz: ").strip()
    if v_oyuncu == '':
        v_oyuncu = "Oyuncu"

    while True:
        p_kullanici_secimi = kullanici_secimi()
        p_bilgisayar_secimi = bilgisayar_secimi()
        print(f"Bilgisayarın seçimi: {p_bilgisayar_secimi}")
        sonuc = kim_kazandi(p_kullanici_secimi, p_bilgisayar_secimi)
        print(sonuc)
        print(f"{v_oyuncu} : {p_kullanici_skor} - Bilgisayar : {p_bilgisayar_skor}")

        if p_kullanici_skor == 3 or p_bilgisayar_skor == 3:
            if p_kullanici_skor == 3:
                print("*** Oyunu siz kazandınız. Tebrikler! ***")
                print("==========================================")
                p_tekrar_oyna = tekrar_oyna()
                if p_tekrar_oyna == "evet":
                    p_kullanici_skor = 0
                    p_bilgisayar_skor = 0
                else:
                    print(f"Oyunumu tercih ettiğiniz için teşekkürler!")
                    break
            elif p_bilgisayar_skor == 3:
                print("Üzgünüm. Oyunu bilgisayar kazandı!")
                print("==========================================")
                p_tekrar_oyna = tekrar_oyna()
                if p_tekrar_oyna == "evet":
                    p_kullanici_skor = 0
                    p_bilgisayar_skor = 0
                else:
                    print(f"Oyunumu tercih ettiğiniz için teşekkürler!")
                    break
        else:
            p_tekrar_oyna = tekrar_oyna()
            if p_tekrar_oyna != "evet":
                print(f"Oyunumu tercih ettiğiniz için teşekkürler!")
                break

tas_kagit_makas_oyna()