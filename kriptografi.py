def remove_duplicates_and_extend(text):
    text = ''.join(char.lower() for char in text if char.isalpha())

    unique_chars = []
    for char in text:
        if char not in unique_chars:
            unique_chars.append(char)

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in unique_chars:
            unique_chars.append(char)

    return ''.join(unique_chars)

def create_monoalphabetic_cipher(key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher = {}
    for i, char in enumerate(alphabet):
        if i < len(key):
            cipher[char] = key[i]
        else:
            cipher[char] = char

    return cipher

def encrypt_with_monoalphabetic(text, cipher):
    encrypted_text = []
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            new_char = cipher.get(char, char)
            if is_upper:
                new_char = new_char.upper()
            encrypted_text.append(new_char)
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)

def decrypt_with_monoalphabetic(text, cipher):
    decrypted_text = []
    reverse_cipher = {v: k for k, v in cipher.items()}

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            new_char = reverse_cipher.get(char, char)
            if is_upper:
                new_char = new_char.upper()
            decrypted_text.append(new_char)
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)

while True:
    choice = input("Ketik 'E' untuk enkripsu atau 'D' untuk dekripsi (K untuk keluar): ").strip().lower()

    if choice == 'e':
        user_key = input("Kata Kunci: ")
        processed_text = remove_duplicates_and_extend(user_key)
        key = processed_text
        cipher = create_monoalphabetic_cipher(key)
        user_input = input("Masukkan Teks yang akan dienkripsi: ")
        encrypted_text = encrypt_with_monoalphabetic(user_input, cipher)
        print("Teks terenkripsi: " + encrypted_text)
    elif choice == 'd':
        user_key = input("Kata Kunci: ")
        processed_text = remove_duplicates_and_extend(user_key)
        key = processed_text
        cipher = create_monoalphabetic_cipher(key)
        user_input = input("Masukkan Teks yang akan didekripsi: ")
        decrypted_text = decrypt_with_monoalphabetic(user_input, cipher)
        print("Teks terdekripsi: " + decrypted_text)
    elif choice == 'k':
        break
    else:
        print("Gada cuy, Ketik 'E' untuk enkripsi atau 'D' untuk dekripsi (K untuk keluar)")
