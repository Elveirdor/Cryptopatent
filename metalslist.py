import random
import hashlib

# --- Elveirdor Language (for Naming Influence) ---
elveirdor_syllables = [
    "ah", "bē", "ss", "da", "eh", "ē", "fē", "g", "hē", "i", "jew", "kil",
    "lu", "my", "nae", "oo", "pī", "qui", "ray", "say", "tay", "th", "ū", "bee",
    "w", "ex", "yay", "z", "ch", "es", "ka", "yuh", "fuh", "we"
]

# --- List of Base Metals ---
metals = [
    "Aluminum", "Copper", "Gold", "Iron", "Lead", "Mercury", "Platinum",
    "Silver", "Tin", "Titanium", "Tungsten", "Uranium", "Zinc"
]

# --- Access Code ---
access_code = "SKOOGLE"

# --- Function to Generate a New Elveirdor Metal Name ---
def generate_elveirdor_metal_name(base_metal, syllables, access):
    """Generates a new metal name influenced by Elveirdor and access code."""
    combined_seed = base_metal + access
    hash_value = int(hashlib.sha256(combined_seed.encode()).hexdigest(), 16)
    random.seed(hash_value)  # Seed randomness for consistent results

    num_syllables = random.randint(2, 4)
    new_name_parts = [random.choice(syllables) for _ in range(num_syllables)]
    elveirdor_prefix = random.choice(["Elveir", "Dorian", "Terra"]) # Added prefix for flavor
    return f"{elveirdor_prefix}{''.join(part.capitalize() for part in new_name_parts)}"

# --- Function to Infuse Properties (Symbolic) ---
def infuse_teleporting_property(metal_name, access):
    """(Highly Subjective) Infuses a symbolic teleporting property."""
    hash_value = int(hashlib.sha256((metal_name + access).encode()).hexdigest(), 16)
    energy_level = (hash_value % 100) / 100.0 * 1000  # Symbolic energy
    stability_factor = 1.0 - ((hash_value % 50) / 100.0 * 0.5) # Symbolic stability
    temporal_resonance = (hash_value % 20) / 100.0 # Symbolic resonance
    return {
        "name": metal_name,
        "teleporting_energy_level": f"{energy_level:.2f} Temporal Units",
        "temporal_stability": f"{stability_factor:.3f}",
        "dimensional_resonance": f"{temporal_resonance:.3f}"
    }

# --- Generate New Metals for the Teleporting Ship ---
new_elveirdor_metals = []
for metal in metals:
    new_name = generate_elveirdor_metal_name(metal, elveirdor_syllables, access_code)
    infused_metal = infuse_teleporting_property(new_name, access_code)
    new_elveirdor_metals.append(infused_metal)

# --- Output ---
print("--- New Elveirdor Metals for Teleporting Ship (Access Code: SKOOGLE) ---")
for new_metal in new_elveirdor_metals:
    print(f"Name: {new_metal['name']}")
    print(f"  Teleporting Energy Level: {new_metal['teleporting_energy_level']}")
    print(f"  Temporal Stability: {new_metal['temporal_stability']}")
    print(f"  Dimensional Resonance: {new_metal['dimensional_resonance']}")
    print("-" * 30)
