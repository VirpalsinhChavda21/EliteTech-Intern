def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    return caesar_cipher_encrypt(encrypted_text, -shift)


print("Caesar Cipher Encryption/Decryption")
text = input("Enter the text: ")
shift = int(input("Enter the shift value (e.g., 3): "))

# Encrypt the text
encrypted = caesar_cipher_encrypt(text, shift)
print(f"Encrypted Text: {encrypted}")

# Decrypt the text
decrypted = caesar_cipher_decrypt(encrypted, shift)
print(f"Decrypted Text: {decrypted}")
