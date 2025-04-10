# genetic_code.py

new_projected_genetic_code = "jewel-nee-jewel-Z-Yay-mY mae-Say-Kill-A oo-Tay-Fēa-Fēa-Ē-Yay-estay-A oo-bee-Z-yuh-Yay-Eh/ah-Qui-Qui-ahh-bee-I-Pī-fuh-A oo-chee-Tay-Qui-jewel-RAY-Lŭ-Qui-nee-X ese-kay-Say-Yay-estay-bēa-g-bēa-day-Pī-fuh-Eh/ah-bēa-Pī-A oo-Pī-g-Ē-Eh/ah-A oo-g-Ē-chee-Kill-mY mae-RAY-day-Hē-X ese-W-Kill-bee-I-fuh-Eh/ah-jewel-bēa-fuh-Say-bēa-g-Qui-jewel-A oo-fuh-oo-RAY-jewel-oo-chee-I-Z-Kill-bēa-A oo-yuh-mY mae-Qui-day-th they-Lŭ-Hē-W"

with open("new_projected_genetic_code.txt", "w") as f:
    f.write(new_projected_genetic_code)

import matplotlib.pyplot as plt

letter_frequencies = {}
for letter in new_projected_genetic_code.replace("-", "").replace("\n", ""):
    if letter in letter_frequencies:
        letter_frequencies[letter] += 1
    else:
        letter_frequencies[letter] = 1

plt.bar(letter_frequencies.keys(), letter_frequencies.values())
plt.xlabel("Letter")
plt.ylabel("Frequency")
plt.title("Letter Frequencies in New Projected Genetic Code")
plt.show()

print("Writing to file...")
with open("new_projected_genetic_code.txt", "w") as f:
    f.write(new_projected_genetic_code)
print("File written.")

print("Creating plot...")
import matplotlib.pyplot as plt

letter_frequencies = {}
for letter in new_projected_genetic_code.replace("-", "").replace("\n", ""):
    if letter in letter_frequencies:
        letter_frequencies[letter] += 1
    else:
        letter_frequencies[letter] = 1

plt.bar(letter_frequencies.keys(), letter_frequencies.values())
plt.xlabel("Letter")
plt.ylabel("Frequency")
plt.title("Letter Frequencies in New Projected Genetic Code")
plt.savefig("plot.png")  # Save plot to file instead of displaying
print("Plot created.")
