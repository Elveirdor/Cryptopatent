# Elveirdor Language Script

# Define the Elveirdor alphabet
elveirdor_alphabet = {
    'A': 'ahh',
    'E': 'Eh/ah',
    'EE': 'Ē',
    'I': 'I',
    'O': 'A oo',
    'U': 'oo',
    'B': 'bea',
    'C': 'SSS',
    'D': 'day',
    'F': 'Fea',
    'G': 'g',
    'H': 'Hee',
    'J': 'jewel',
    'K': 'Kill',
    'L': 'Lŭ',
    'M': 'my mae',
    'N': 'nee',
    'P': 'Pī',
    'Q': 'Qui',
    'R': 'RAY',
    'S': 'Say',
    'T': 'Tay',
    'Th': 'th they',
    'V': 'bee',
    'W': 'W',
    'X': 'X ese',
    'Y': 'Yay',
    'Z': 'Z',
    'Ch': 'chee',
    'LL': 'yuh',
    'Ph': 'fuh',
    'Wh': 'we-sand',
    'st': 'estay',
    'ck': 'kay'
}

# Define the cryptographic code
image_hash = "3421a8d9e2c71b45f6e3d4c2b1a0f8e7"
image_code = "ELA001"

# Define the image description
image_description = "The image shows a piece of lined paper with handwritten notes, featuring an alphabet chart with letters and symbols, on a green fabric background."

# Define the Elveirdor text
elveirdor_text = "jewel-nee-jewel-Z-Yay-mY mae-Say-Kill-A oo-Tay-Fēa-Fēa-Ē-Yay-estay-A oo-bee-Z-yuh-Yay-Eh/ah-Qui-Qui-ahh-bee-I-Pī-fuh-A oo-chee-Tay-Qui-jewel-RAY-Lŭ-Qui-nee-X ese-kay-Say-Yay-estay-bēa-g-bēa-day-Pī-fuh-Eh/ah-bēa-Pī-A oo-Pī-g-Ē-Eh/ah-A oo-g-Ē-chee-Kill-mY mae-RAY-day-Hē-X ese-W-Kill-bee-I-fuh-Eh/ah-jewel-bēa-fuh-Say-bēa-g-Qui-jewel-A oo-fuh-oo-RAY-jewel-oo-chee-I-Z-Kill-bēa-A oo-yuh-mY mae-Qui-day-th they-Lŭ-Hē-W"

# Print the Elveirdor alphabet
print("Elveirdor Alphabet:")
for key, value in elveirdor_alphabet.items():
    print(f"{key}: {value}")

# Print the cryptographic code
print("\nCryptographic Code:")
print(f"IMAGE_HASH: {image_hash}")
print(f"IMAGE_CODE: {image_code}")

# Print the image description
print("\nImage Description:")
print(image_description)

# Print the Elveirdor text
print("\nElveirdor Text:")
print(elveirdor_text)
