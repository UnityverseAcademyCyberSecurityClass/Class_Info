from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Anahtar üretme (3DES anahtarı 16 veya 24 byte olmalıdır)
key = get_random_bytes(24)

# Veri şifrelenecek metin
plaintext = "Merhaba Dünya! 3DES şifreleme örneği."

# 3DES için bir cipher nesnesi oluşturma (CBC modunda)
cipher = DES3.new(key, DES3.MODE_CBC)

# Veriyi şifreleme
ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), DES3.block_size))

# Şifrelenmiş veriyi ve başlangıç vektörünü (IV) gösterme
print("Şifreli Metin:", ciphertext.hex())
print("Anahtar (hex):", key.hex())
print("IV (hex):", cipher.iv.hex())

# Şifre çözme işlemi (IV ve key ile birlikte)
cipher_decrypt = DES3.new(key, DES3.MODE_CBC, iv=cipher.iv)
decryptedtext = unpad(cipher_decrypt.decrypt(ciphertext), DES3.block_size)

# Çözülmüş metni gösterme
print("Çözülmüş Metin:", decryptedtext.decode('utf-8'))
