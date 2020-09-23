from string import ascii_lowercase
from re import sub

encoder = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])
decoder = str.maketrans(ascii_lowercase[::-1], ascii_lowercase)


def encode(plain_text):
    encoded_string = plain_text.lower().translate(encoder)
    encoded_string = sub(r'[^\w]', '', encoded_string)
    cipher_text = sub(r'(.{5})', r'\1 ', encoded_string).strip()
    return cipher_text


def decode(ciphered_text):
    return ciphered_text.replace(' ', '').translate(decoder)
