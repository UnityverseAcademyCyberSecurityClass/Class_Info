from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# 3DES anahtarımız:
key = get_random_bytes(24)

plaintext = "Bu cümleyi 3DES algoritmasını kullanarak şifreleyeceğiz."
cipher = DES3.new(key, DES3.MODE_CBC)

# Şifreleme:
ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), DES3.block_size))

# Şifreleme sonucunu ve başlangıç vektörünü print edelim.
print("Şifrelenmiş metin (hex): ", ciphertext.hex())
print("Anahtar (hex): ", key.hex())
print("IV / Başlangıç vektörü (hex): ", cipher.iv.hex())

# Deşifre etme:
cipher_decrypt = DES3.new(key, DES3.MODE_CBC, iv = cipher.iv)
decryptedtext = unpad(cipher_decrypt.decrypt(ciphertext), DES3.block_size)

# Deşifre edilmiş metni print edelim.
print("Deşifre edilmiş metin: ", decryptedtext.decode('utf-8'))




