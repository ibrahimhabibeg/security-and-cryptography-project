from .utils import char_to_idx, idx_to_char


def caesar_encrypt(plaintext, key):
    ciphertext = ""
    for c in plaintext:
        if c.isalpha():
            shifted_idx = (char_to_idx(c) + key) % 26
            encrypted_char = idx_to_char(shifted_idx)
            if c.isupper():
                encrypted_char = encrypted_char.upper()
            ciphertext += encrypted_char
        else:
            ciphertext += c
    return ciphertext


def caesar_decrypt(ciphertext, key):
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            shifted_idx = (char_to_idx(c) - key) % 26
            decrypted_char = idx_to_char(shifted_idx)
            if c.isupper():
                decrypted_char = decrypted_char.upper()
            plaintext += decrypted_char
        else:
            plaintext += c
    return plaintext
