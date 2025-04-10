import random

# Define the Elveirdor letters
elveirdor_letters = {
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

# Define the Ship class
class Ship:
    def __init__(self, name, ship_id, online_id, material_id, specifications):
        self.name = name
        self.ship_id = ship_id
        self.online_id = online_id
        self.material_id = material_id
        self.specifications = specifications

# Define the Fleet class
class Fleet:
    def __init__(self, name):
        self.name = name
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

    def teleport(self, destination):
        print(f"Teleporting {self.name} fleet to {destination}...")

# Define the ElveirdorFleet class
class ElveirdorFleet(Fleet):
    def __init__(self):
        super().__init__("Elveirdor")

    def regime(self):
        print("Elveirdor Fleet Regime:")
        print("Explore galaxy, defend against threats, engage in trade.")

# Generate a random genetic code
def generate_genetic_code(length):
    genetic_code = ''
    for _ in range(length):
        letter = random.choice(list(elveirdor_letters.keys()))
        genetic_code += elveirdor_letters[letter] + '-'
    return genetic_code[:-1]

# Project the genetic code 70,000 years past 2025
def project_genetic_code(genetic_code, years):
    projected_genetic_code = ''
    for _ in range(years):
        projected_genetic_code += genetic_code + '\n'
    return projected_genetic_code

# Create ships
elveirdor = Ship("Elveirdor", "75298484751231232975", "2975848475@123123@2975", "29758484751231232975", {
    "shape": "Flat on top and bottom",
    "glass_squares": "Slightly stretched out glass squares"
})
comb = Ship("Comb", "75298484751231232975", "2975848475@123123@2975", "29758484751231232975", {
    "shape": "Flat on top and bottom",
    "captains_window": "Facing the sun with thick glass"
})
juan_60s = Ship("Juan 60's", "75298484751231232975", "2975848475@123123@2975", "29758484751231232975", {
    "shape": "Similar to Comb ship",
    "cuts": "Cuts from outside to inside"
})
sonic = Ship("Sonic", "75298484751231232975", "2975848475@123123@2975", "29758484751231232975", {
    "shape": "Similar to Speedway big gulp cup",
    "rotating_floorboards": "Inside that align with doorways"
})

# Create fleet
elveirdor_fleet = ElveirdorFleet()
elveirdor_fleet.add_ship(comb)
elveirdor_fleet.add_ship(elveirdor)
elveirdor_fleet.add_ship(juan_60s)
elveirdor_fleet.add_ship(sonic)

# Create fleet
elveirdor_fleet = ElveirdorFleet()

# Add ships to the fleet
ships = [elveirdor, comb, juan_60s, sonic]
for ship in ships:
    elveirdor_fleet.add_ship(ship)
print("Elveirdor Fleet:")
for ship in elveirdor_fleet.ships:
    print(f"Ship: {ship.name}")
    print(f"Ship ID: {ship.ship_id}")
    print(f"Specifications: {ship.specifications}")

print("\nProjected Genetic Code:")
genetic_code = generate_genetic_code(100)
projected_genetic_code = project_genetic_code(genetic_code, 70000)
print(projected_genetic_code)

# Save the projected genetic code to a file
with open("projected_genetic_code.txt", "w") as f:
    f.write(projected_genetic_code)

# Visualize the results
import matplotlib.pyplot as plt

# Count the frequency of each letter in the projected genetic code
letter_frequencies = {}
for letter in projected_genetic_code:
    if letter in letter_frequencies:
        letter_frequencies[letter] += 1
    else:
        letter_frequencies[letter] = 1

# Plot a bar chart of the letter frequencies
plt.bar(letter_frequencies.keys(), letter_frequencies.values())
plt.xlabel("Letter")
plt.ylabel("Frequency")
plt.title("Letter Frequencies in Projected Genetic Code")
plt.show()

# ... (rest of your script remains the same)

# Save the projected genetic code to a file
with open("projected_genetic_code.txt", "w") as f:
    f.write(projected_genetic_code)

# Visualize the results
import matplotlib.pyplot as plt

# Count the frequency of each letter in the projected genetic code
letter_frequencies = {}
for letter in projected_genetic_code.replace("-", "").replace("\n", ""):
    if letter in letter_frequencies:
        letter_frequencies[letter] += 1
    else:
        letter_frequencies[letter] = 1

# Plot a bar chart of the letter frequencies
plt.bar(letter_frequencies.keys(), letter_frequencies.values())
plt.xlabel("Letter")
plt.ylabel("Frequency")
plt.title("Letter Frequencies in Projected Genetic Code")
plt.show()
