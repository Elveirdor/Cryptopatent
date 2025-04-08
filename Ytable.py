import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

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

    def add_nested_row(self, row_name, nested_row_name, data):
        if row_name in self.table:
            if isinstance(self.table[row_name], dict):
                self.table[row_name][nested_row_name] = data
            else:
                print("Row is not a dictionary")
        else:
            print("Row not found")

    def get_nested_row(self, row_name, nested_row_name):
        if row_name in self.table:
            if isinstance(self.table[row_name], dict):
                return self.table[row_name].get(nested_row_name)
            else:
                print("Row is not a dictionary")
        else:
            print("Row not found")

    def train_model(self, row_name):
        if row_name in self.table:
            data = self.table[row_name]
            X = pd.DataFrame(data["X"])
            y = pd.DataFrame(data["y"])
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            model = LinearRegression()
            model.fit(X_train, y_train)
            return model
        else:
            print("Row not found")

    def caesar_cipher(self, row_name, shift):
        if row_name in self.table:
            data = self.table[row_name]
            encoded_data = ""
            for char in data:
                if char.isalpha():
                    ascii_offset = 65 if char.isupper() else 97
                    encoded_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                    encoded_data += encoded_char
                else:
                    encoded_data += char
            return encoded_data
        else:
            print("Row not found")

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

# Example usage
y_table = YTable()

y_table.add_row("Row 1", {"X": [[1, 2], [3, 4], [5, 6]], "y": [2, 4, 5]})

y_table.print_table()

model = y_table.train_model("Row 1")

print(model.coef_)

y_table.add_row("Row 2", "Hello, World!")

y_table.print_table()

encoded_data = y_table.caesar_cipher("Row 2", 3)

print(encoded_data)

encoded_data = y_table.elveirdor_alphabet("Row 2")

print(encoded_data)
