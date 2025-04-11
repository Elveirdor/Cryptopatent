import random
import datetime
import hashlib

# --- Parameters ---
projection_interval = 2000
num_symbolic_projections = 5
genetic_code_length = 50  # Shorter for food chain
num_food_chain_levels = 5
simulation_years = 70000

# --- Elveirdor Letters (Symbolic Representation of Organisms) ---
elveirdor_letters = {
    'A': 'Apex Predator', 'B': 'Large Herbivore', 'C': 'Small Herbivore',
    'D': 'Producer (Plant)', 'E': 'Decomposer', 'F': 'Scavenger',
    'G': 'Insectivore', 'H': 'Carnivorous Insect', 'I': 'Fungi',
    'J': 'Microorganism', 'K': 'Water Source', 'L': 'Sunlight'
}
elveirdor_keys = list(elveirdor_letters.keys())

# --- Symbolic Event Functions (Modified for Environmental Influence) ---
def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def interpret_environment(year):
    """(Highly Subjective) Interprets the 'environmental conditions' based on the year."""
    seed = year % 1000  # Simple cycle
    if seed < 300:
        return {"resource_abundance": random.uniform(0.8, 1.2), "climate_stress": random.uniform(0.1, 0.3)}
    elif seed < 700:
        return {"resource_abundance": random.uniform(0.5, 0.9), "climate_stress": random.uniform(0.4, 0.7)}
    else:
        return {"resource_abundance": random.uniform(0.2, 0.6), "climate_stress": random.uniform(0.7, 1.0)}

def evolve_organism(organism_code, environment):
    """(Highly Subjective) Simulates a simple form of 'evolution' based on environment."""
    mutation_rate = environment["climate_stress"] * 0.05
    if random.random() < mutation_rate:
        organism_list = list(organism_code)
        mutation_index = random.randint(0, len(organism_list) - 1)
        organism_list[mutation_index] = random.choice(elveirdor_keys)
        return "".join(organism_list)
    return organism_code

# --- Genetic Code Functions (representing initial organism traits) ---
def generate_genetic_code(length):
    genetic_code = ''.join(random.choice(elveirdor_keys) for _ in range(length))
    return genetic_code

# --- Food Chain Simulation ---
def simulate_food_chain(initial_organisms, years):
    food_chain_history = {}
    current_organisms = {level: generate_genetic_code(genetic_code_length) for level in range(num_food_chain_levels)}

    for year_offset in range(years):
        year = datetime.datetime.now().year + 1 + year_offset
        environment = interpret_environment(year)
        food_chain_state = {}

        for level, organism_code in current_organisms.items():
            evolved_code = evolve_organism(organism_code, environment)
            current_organisms[level] = evolved_code
            food_chain_state[level] = [elveirdor_letters.get(gene, "Unknown") for gene in evolved_code]

        food_chain_history[year] = food_chain_state

        if year % 10000 == 0:
            print(f"\n--- Food Chain State at Year {year} ---")
            for level, organisms in food_chain_state.items():
                print(f"Level {level + 1}: {', '.join(organisms[:10])}...") # Print a snippet

    return food_chain_history

# --- Main Execution ---
if __name__ == "__main__":
    print("--- 70,000 Year Symbolic Food Chain Simulation ---")
    initial_organisms = {level: generate_genetic_code(genetic_code_length) for level in range(num_food_chain_levels)}
    food_chain_data = simulate_food_chain(initial_organisms, simulation_years)

    print("\n--- Simulation Complete. (Detailed history in 'food_chain_data' variable) ---")
