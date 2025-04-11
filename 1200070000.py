import hashlib
import datetime
import random

# --- Parameters ---
projection_interval = 2000  # Years for symbolic events
num_symbolic_projections = 5
genetic_projection_years = 70000
genetic_code_length = 100
num_genetic_code_prints = 2000

# --- Elveirdor Letters ---
elveirdor_letters = {
    'A': 'ahh', 'B': 'bēa', 'C': 'SSS', 'D': 'day', 'E': 'Eh/ah', 'EE': 'Ē',
    'F': 'Fēa', 'G': 'g', 'H': 'Hē', 'I': 'I', 'J': 'jewel', 'K': 'Kill',
    'L': 'Lŭ', 'M': 'mY mae', 'N': 'nee', 'O': 'A oo', 'P': 'Pī', 'Q': 'Qui',
    'R': 'RAY', 'S': 'Say', 'T': 'Tay', 'Th': 'th they', 'U': 'oo', 'V': 'bee',
    'W': 'W', 'X': 'X ese', 'Y': 'Yay', 'Z': 'Z', 'CH': 'chee', 'ST': 'estay',
    'Ck': 'kay', 'LL': 'yuh', 'ph': 'fuh', 'wh': 'we'
}

# --- Genetic Code Generation ---
def generate_genetic_code(length):
    genetic_code = ''
    for _ in range(length):
        letter = random.choice(list(elveirdor_letters.keys()))
        genetic_code += elveirdor_letters[letter] + '-'
    return genetic_code[:-1]

# --- Symbolic Event Functions ---
def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def interpret_image(image_description):
    values = {}
    if "lined paper" in image_description:
        values['paper'] = 1
    if "alphabet" in image_description:
        values['alphabet'] = 26
    if "green" in image_description:
        values['green'] = 7
    if "fabric" in image_description:
        values['fabric'] = 3
    return values

def combine_codes(code1, code2):
    combined = code1 + code2
    return generate_hash(combined)[:10]

def project_symbolic_events(image_interpretation, combined_code, interval, num_projections):
    seed = int(combined_code, 16)
    year_offset = seed % interval
    current_year = datetime.datetime.now().year
    first_projection_year = ((current_year // interval) + 1) * interval + year_offset

    projections = []
    for i in range(num_projections):
        projection_year = first_projection_year + (i * interval)
        event_hash = generate_hash(f"{image_interpretation}-{combined_code}-{projection_year}")[:8]
        projections.append(f"Year: {projection_year}, Symbolic Event Hash: {event_hash}")
    return projections

# --- Genetic Code Projection ---
def project_genetic_code(genetic_code, years):
    projected_codes = []
    current_year = datetime.datetime.now().year
    for i in range(years):
        projected_year = current_year + 1 + i
        projected_codes.append(f"Year: {projected_year}: {genetic_code}")
    return projected_codes

# --- Main Execution (Modified to run only symbolic events) ---
if __name__ == "__main__":
    # --- Symbolic Event Projection ---
    image_description = "The image shows a piece of lined paper with handwritten notes, featuring an alphabet chart with letters and symbols, on a green fabric background."
    code_no_bang = "NOBANG"
    code_skoogle = "SKOOGLE"

    image_values = interpret_image(image_description)
    combined_code = combine_codes(code_no_bang, code_skoogle)
    symbolic_projections = project_symbolic_events(
        image_values, combined_code, projection_interval, num_symbolic_projections
    )

    print("--- Symbolic Event Projections ---")
    print("Image Interpretation Values:", image_values)
    print("Combined Code Hash:", combined_code)
    for projection in symbolic_projections:
        print(projection)

    # --- Genetic Code Projection (Commented Out) ---
    # print("\n--- Genetic Code Projection (First 2000 Years) ---")
    # genetic_code = generate_genetic_code(genetic_code_length)
    # genetic_projections = project_genetic_code(genetic_code, num_genetic_code_prints)
    # for projection in genetic_projections:
    #     print(projection)
