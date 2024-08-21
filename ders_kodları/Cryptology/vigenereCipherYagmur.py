def key_generator(message, key):

    message = list(message)  # inputları char listesi olarak depolamak için.
    key = list(key)

    # anahtarın uzunluğu = mesajın uzunluğu şartı sağlanmak zorunda. bu durumu inceleyelim:
    if len(key) == len(message):
        return "".join(key)
    
    elif len(key) > len(message):
        shortened_key = []
        for i in range(len(key) - len(message) + 1):
            shortened_key.append(key[i])
        
        return "".join(shortened_key)
    
    else:   # len(key) < len(message)
        long_key = key
        for i in range(len(message) - len(key)):   # message ve key arasındaki FARK kadar eklemeli.
            long_key.append(key[i % len(key)])   # key uzunluğu ile mod al ki, eklerken kendini tekrarlayarak eklesin. (örn. key -> keykeyk (message length = 7 ise))

        return "".join(long_key)


def encrypt(message, key):

    encrypted_message = []
    key = key_generator(message, key)

    for i in range(len(message)):
        msgchar = message[i]
        if msgchar.isupper():
            encrypted_char_index_no = ((ord(msgchar) - ord('A')) + (ord(key[i]) - ord('A'))) % 26   # alfabetik index no. birimi üzerinden hesaplama.
            encrypted_char_ASCII = encrypted_char_index_no + ord('A')   # birim dönüşümü: index no.'dan ASCII kodu değerine dönüşüm.
            encrypted_char = chr(encrypted_char_ASCII)
    
        elif msgchar.islower():
            encrypted_char_index_no = ((ord(msgchar) - ord('a')) + (ord(key[i]) - ord('a'))) % 26   # alfabetik index no. birimi üzerinden hesaplama.
            encrypted_char_ASCII = encrypted_char_index_no + ord('a')   # birim dönüşümü: index no.'dan ASCII kodu değerine dönüşüm.
            encrypted_char = chr(encrypted_char_ASCII)

        else:
            encrypted_char = msgchar   # eğer mesajdaki karakter, harf değil ise.

        encrypted_message.append(encrypted_char)

    #return "".join(encrypted_message)
    encrypted_message = "".join(encrypted_message)
    return encrypted_message


def decrypt(encrypted_message, key):

    decrypted_message = []
    key = key_generator(encrypted_message, key)

    for i in range(len(encrypted_message)):
        enchar = encrypted_message[i]
        if enchar.isupper():
            decrypted_char_index_no = ((ord(enchar) - ord('A')) - (ord(key[i]) - ord('A'))) % 26
            decrypted_char_ASCII = decrypted_char_index_no + ord('A')
            decrypted_char = chr(decrypted_char_ASCII)

        elif enchar.islower():
            decrypted_char_index_no = ((ord(enchar) - ord('a')) - (ord(key[i]) - ord('a'))) % 26
            decrypted_char_ASCII = decrypted_char_index_no + ord('a')
            decrypted_char = chr(decrypted_char_ASCII)

        else: 
            decrypted_char = enchar

        decrypted_message.append(decrypted_char)

    decrypted_message = "".join(decrypted_message)
    return decrypted_message


# Örnekler ile test edelim.

# 1. ihtimal: uzun mesaj, kısa anahtar.
text = "testmetni"
key = "an"

print("Plaintext: ", text)
print("Key given as input: ", key)
print("Key to be used: ", key_generator(text, key))
print("\n")

encrypted_text = encrypt(text, key)
print("Encrypted text: ", encrypted_text)
decrypted_text = decrypt(encrypted_text, key)
print("Decrypted text: ", decrypted_text)
print("\n******************************\n")

# 2. ihtimal: kısa mesaj, uzun anahtar.
text = "test"
key = "anahtar"

print("Plaintext: ", text)
print("Key given as input: ", key)
print("Key to be used: ", key_generator(text, key))
print("\n")

encrypted_text = encrypt(text, key)
print("Encrypted text: ", encrypted_text)
decrypted_text = decrypt(encrypted_text, key)
print("Decrypted text: ", decrypted_text)
print("\n******************************\n")

# 3. ihtimal: eşit uzunlukta mesaj ve anahtar.
text = "bumetin"
key = "anahtar"

print("Plaintext: ", text)
print("Key given as input: ", key)
print("Key to be used: ", key_generator(text, key))
print("\n")

encrypted_text = encrypt(text, key)
print("Encrypted text: ", encrypted_text)
decrypted_text = decrypt(encrypted_text, key)
print("Decrypted text: ", decrypted_text)





