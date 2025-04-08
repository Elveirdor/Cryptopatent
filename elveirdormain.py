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

    def print_table(self):
        for row_name, data in self.table.items():
            print(f"{row_name}: {data}")

    def elveirdor_alphabet(self, row_name):
        if row_name in self.table:
            data = self.table[row_name]
            mapping = {
                'A': 'Λ', 'B': 'T', 'C': 'Ψ', 'D': 'R', 'E': 'E', 'F': 'I', 'G': 'N', 'H': 'P', 'I': 'U', 'J': 'B', 'K': 'S',
                'L': '€', 'M': '1', 'N': 'V', 'O': 'O', 'P': 'U', 'Q': 'S', 'R': '7', 'S': 'F', 'T': '9', 'U': '3', 'V': 'Y',
                'W': 'M', 'X': '±', 'Y': 'H', 'Z': 'U', ' ': ' ', ',': ',', '.': '.', '?': '?', '!': '!'
            }
            encoded_data = ""
            for char in data:
                if char.upper() in mapping:
                    encoded_data += mapping[char.upper()]
                else:
                    encoded_data += char
            return encoded_data
        else:
            print("Row not found")

    def train_model(self, row_name):
        if row_name in self.table:
            data = self.table[row_name]
            return data
        else:
            print("Row not found")

def main():
    y_table = YTable()

    y_table.add_row("Row 1", "Hello, World!")

    y_table.print_table()

    encoded_data = y_table.elveirdor_alphabet("Row 1")

    print(encoded_data)

    y_table.add_row("Row 2", {'X': [[1, 2], [3, 4], [5, 6]], 'y': [2, 4, 5]})

    model = y_table.train_model("Row 2")

    print(model)

if __name__ == "__main__":
    main()
