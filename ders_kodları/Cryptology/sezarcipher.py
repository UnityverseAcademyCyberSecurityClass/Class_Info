def sezar_sifreleme(metin, kaydirma):
    sifreli_metin = ""
    for char in metin:
        if char.isalpha():
            kaydirma_turu = 65 if char.isupper() else 97
            sifreli_metin += chr((ord(char) - kaydirma_turu + kaydirma) % 26 + kaydirma_turu)
        else:
            sifreli_metin += char
    return sifreli_metin

def sezar_sifre_cozme(sifreli_metin, kaydirma):
    return sezar_sifreleme(sifreli_metin, -kaydirma)

metin = "Merhaba"
kaydirma = 3
sifreli_metin = sezar_sifreleme(metin, kaydirma)
print("Şifreli Metin:", sifreli_metin)
print("Çözülmüş Metin:", sezar_sifre_cozme(sifreli_metin, kaydirma))
