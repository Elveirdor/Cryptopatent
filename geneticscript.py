import random

# Define the Elveirdor letters
elveirdor_letters = {
    'A': 'ahh', 'B': 'bēa', 'C': 'SSS', 'D': 'day', 'E': 'Eh/ah', 'EE': 'Ē',
    'F': 'Fēa', 'G': 'g', 'H': 'Hē', 'I': 'I', 'J': 'jewel', 'K': 'Kill',
    'L': 'Lŭ', 'M': 'mY mae', 'N': 'nee', 'O': 'A oo', 'P': 'Pī', 'Q': 'Qui',
    'R': 'RAY', 'S': 'Say', 'T': 'Tay', 'Th': 'th they', 'U': 'oo', 'V': 'bee',
    'W': 'W', 'X': 'X ese', 'Y': 'Yay', 'Z': 'Z', 'CH': 'chee', 'ST': 'estay',
    'Ck': 'kay', 'LL': 'yuh', 'ph': 'fuh', 'wh': 'we'
}

# Generate a random genetic code
def generate_genetic_code(length):
    genetic_code = ''
    for _ in range(length):
        letter = random.choice(list(elveirdor_letters.keys()))
        genetic_code += elveirdor_letters[letter] + '-'
    return genetic_code[:-1]  # Remove the trailing '-'

# Project the genetic code 70,000 years past 2025
def project_genetic_code(genetic_code, years):
    projected_genetic_code = ''
    for _ in range(years):
        projected_genetic_code += genetic_code + '\n'
    return projected_genetic_code

# Main function
def main():
    length = 100
    years = 70000
    genetic_code = generate_genetic_code(length)
    projected_genetic_code = project_genetic_code(genetic_code, years)
    print(projected_genetic_code)

if __name__ == "__main__":
    main()
