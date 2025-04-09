class ElveirInterpreter:
    def __init__(self):
        self.elveir_alphabet = {
            'A': 'ahh',
            'B': 'bēa',
            'C': 'SSS',
            'D': 'day',
            'E': 'Eh/ah',
            'EE': 'Ē',
            'F': 'Fēa',
            'G': 'g',
            'H': 'Hē',
            'I': 'I',
            'J': 'jewel',
            'K': 'Kill',
            'L': 'Lŭ',
            'M': 'mY mae',
            'N': 'nee',
            'O': 'A oo',
            'P': 'Pī',
            'Q': 'Qui',
            'R': 'RAY',
            'S': 'Say',
            'T': 'Tay',
            'Th': 'th they',
            'U': 'oo',
            'V': 'bee',
            'W': 'W',
            'X': 'X ese',
            'Y': 'Yay',
            'Z': 'Z',
            'CH': 'chee',
            'ST': 'estay',
            'Ck': 'kay',
            'LL': 'yuh',
            'ph': 'fuh',
            'wh': 'we'
        }

    def english_to_elveir(self, text):
        elveir_text = ''
        i = 0
        while i < len(text):
            if i < len(text) - 1 and text[i:i+2].upper() in self.elveir_alphabet:
                elveir_text += self.elveir_alphabet[text[i:i+2].upper()] + ' '
                i += 2
            elif text[i].upper() in self.elveir_alphabet:
                elveir_text += self.elveir_alphabet[text[i].upper()] + ' '
                i += 1
            else:
                elveir_text += text[i] + ' '
                i += 1
        return elveir_text.strip()

    def elveir_to_english(self, text):
        english_text = ''
        words = text.split()
        reverse_alphabet = {}
        for k, v in self.elveir_alphabet.items():
            if v not in reverse_alphabet:
                reverse_alphabet[v] = k
            else:
                # Handle cases where multiple English letters map to the same Elveir word
                if isinstance(reverse_alphabet[v], list):
                    reverse_alphabet[v].append(k)
                else:
                    reverse_alphabet[v] = [reverse_alphabet[v], k]

        for word in words:
            if word in reverse_alphabet:
                if isinstance(reverse_alphabet[word], list):
                    # For now, just use the first matching English letter
                    english_text += reverse_alphabet[word][0]
                else:
                    english_text += reverse_alphabet[word]
            else:
                english_text += word
        return english_text.lower()

def main():
    interpreter = ElveirInterpreter()
    while True:
        print("Options:")
        print("1. English to Elveir")
        print("2. Elveir to English")
        print("3. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            english_text = input("Enter English text: ")
            elveir_text = interpreter.english_to_elveir(english_text)
            print(f"Elveir: {elveir_text}")
        elif choice == "2":
            elveir_text = input("Enter Elveir text: ")
            english_text = interpreter.elveir_to_english(elveir_text)
            print(f"English: {english_text}")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
