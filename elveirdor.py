# Elveirdor Alphabet Mapping

elveirdor_alphabet = {
    'A': ['ahh', 'ah', 'a', 'uh', 'ahh'],
    'B': ['be', 'bee', 'b'],
    'C': ['sss', 'see', 'c', 'k'],
    'D': ['d', 'day'],
    'E': ['eh', 'e', 'ee'],
    'F': ['f', 'ef', 'fee'],
    'G': ['g', 'gee', 'g(irl)', 'not J(uel)'],
    'H': ['h', 'aitch', 'haitch'],
    'I': ['i', 'eye', 'I'],
    'J': ['j', 'jewel', 'jay'],
    'K': ['k', 'kay', 'kill'],
    'L': ['l', 'el', 'ell'],
    'M': ['m', 'em', 'my'],
    'N': ['n', 'en', 'nee'],
    'O': ['o', 'oh', 'oo'],
    'P': ['p', 'pee', 'pee'],
    'Q': ['q', 'cue', 'kyoo'],
    'R': ['r', 'ar', 'are'],
    'S': ['s', 'es', 'see'],
    'T': ['t', 'tee', 'tee'],
    'U': ['u', 'oo', 'you'],
    'V': ['v', 'vee', 'vee'],
    'W': ['w', 'double u', 'double u'],
    'X': ['x', 'ex', 'ex'],
    'Y': ['y', 'why', 'wah'],
    'Z': ['z', 'zed', 'zee']
}

# Example usage:
print(elveirdor_alphabet['A'])  # Output: ['ahh', 'ah', 'a', 'uh', 'ahh']
print(elveirdor_alphabet['Z'])  # Output: ['z', 'zed', 'zee']

# Define the Elveirdor Alphabet
elveirdor_alphabet = {
    'A': 'Λ', 'B': 'T', 'C': 'Ψ', 'D': 'R', 'E': 'E', 'F': 'I', 'G': 'N', 'H': 'P', 'I': 'U', 'J': 'B', 'K': 'S',
    'L': '€', 'M': '1', 'N': 'V', 'O': 'O', 'P': 'U', 'Q': 'S', 'R': '7', 'S': 'F', 'T': '9', 'U': '3', 'V': 'Y',
    'W': 'M', 'X': '±', 'Y': 'H', 'Z': 'U', ' ': ' ', ',': ',', '.': '.', '?': '?', '!': '!'
}

# Function to encode a message using the Elveirdor Alphabet
def encode_message(message):
    encoded_message = ""
    for char in message.upper():
        if char in elveirdor_alphabet:
            encoded_message += elveirdor_alphabet[char]
        else:
            encoded_message += char
    return encoded_message

# Function to decode a message using the Elveirdor Alphabet
def decode_message(message):
    decoded_message = ""
    reverse_alphabet = {v: k for k, v in elveirdor_alphabet.items()}
    for char in message:
        if char in reverse_alphabet:
            decoded_message += reverse_alphabet[char]
        else:
            decoded_message += char
    return decoded_message

# Test the functions
message = "Hello, World!"
encoded_message = encode_message(message)
decoded_message = decode_message(encoded_message)

print(f"Original Message: {message}")
print(f"Encoded Message: {encoded_message}")
print(f"Decoded Message: {decoded_message}")


def caesar_cipher(message, shift):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encoded_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encoded_message += encoded_char
        else:
            encoded_message += char
    return encoded_message

def elveirdor_alphabet(message):
    # Elveirdor Alphabet mapping
    mapping = {
        'A': 'Λ', 'B': 'T', 'C': 'Ψ', 'D': 'R', 'E': 'E', 'F': 'I', 'G': 'N', 'H': 'P', 'I': 'U', 'J': 'B', 'K': 'S',
        'L': '€', 'M': '1', 'N': 'V', 'O': 'O', 'P': 'U', 'Q': 'S', 'R': '7', 'S': 'F', 'T': '9', 'U': '3', 'V': 'Y',
        'W': 'M', 'X': '±', 'Y': 'H', 'Z': 'U', ' ': ' ', ',': ',', '.': '.', '?': '?', '!': '!'
    }
    encoded_message = ""
    for char in message:
        if char.upper() in mapping:
            encoded_message += mapping[char.upper()]
        else:
            encoded_message += char
    return encoded_message

def encode_message(message, shift):
    caesar_encoded_message = caesar_cipher(message, shift)
    elveirdor_encoded_message = elveirdor_alphabet(caesar_encoded_message)
    return elveirdor_encoded_message

def main():
    print("Encoding System")
    print("----------------")
    message = input("Enter a message: ")
    shift = int(input("Enter a shift value: "))
    encoded_message = encode_message(message, shift)
    print(f"Encoded Message: {encoded_message}")

if __name__ == "__main__":
    main()
