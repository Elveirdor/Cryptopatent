mapping = {
    'A': 'Λ', 'B': 'T', 'C': 'Ψ', 'D': 'R', 'E': 'E', 'F': 'I', 'G': 'N', 'H': 'P', 'I': 'U', 'J': 'B', 'K': 'S',
    'L': '€', 'M': '1', 'N': 'V', 'O': 'O', 'P': 'U', 'Q': 'S', 'R': '7', 'S': 'F', 'T': '9', 'U': '3', 'V': 'Y',
    'W': 'M', 'X': '±', 'Y': 'H', 'Z': 'U', ' ': ' ', ',': ',', '.': '.', '?': '?', '!': '!',
    'a': 'λ', 'b': 't', 'c': 'ψ', 'd': 'r', 'e': 'e', 'f': 'i', 'g': 'n', 'h': 'p', 'i': 'u', 'j': 'b', 'k': 's',
    'l': '€', 'm': '1', 'n': 'v', 'o': 'o', 'p': 'u', 'q': 's', 'r': '7', 's': 'f', 't': '9', 'u': '3', 'v': 'y',
    'w': 'm', 'x': '±', 'y': 'h', 'z': 'u'
}

class YTable:
    def __init__(self):
        self.table = {}

    def add_row(self, row_name, data):
        self.table[row_name] = data

    def get_row(self, row_name):
        return self.table.get(row_name)

    def update_row(self, row_name, data):
        if row_name in self.table:
            self.table[row_name] = data
        else:
            print("Row not found")

    def delete_row(self, row_name):
        if row_name in self.table:
            del self.table[row_name]
        else:
            print("Row not found")

    def search_rows(self, query):
        results = []
        for row_name, data in self.table.items():
            if query in data:
                results.append((row_name, data))
        return results

    def filter_rows(self, filter_func):
        results = []
        for row_name, data in self.table.items():
            if filter_func(data):
                results.append((row_name, data))
        return results

def compress_text(text):
    compressed_text = ""
    for char in text:
        if char in mapping:
            compressed_text += mapping[char]
        else:
            compressed_text += char
    return compressed_text

text = "Hello, World!"
compressed_text = compress_text(text)
print(compressed_text)

