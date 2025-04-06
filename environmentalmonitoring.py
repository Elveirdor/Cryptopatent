import requests

# WAQI API endpoint
url = "https://api.waqi.info/feed/beijing/"

# API token
token = "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"

# Send GET request to API endpoint
response = requests.get(url, params={"token": token})

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()

    # Print the entire JSON response
    print(data)
else:
    print("Failed to retrieve data:", response.status_code)
import numpy as np

# Define a function to simulate energy circulation
def simulate_energy_circulation():
    # Initialize variables
    energy_level = 0
    circulation_pattern = np.zeros((360, 180))  # 360 degrees longitude, 180 degrees latitude

    # Simulate energy flow
    for i in range(360):
        for j in range(180):
            # Calculate energy level at each point
            energy_level += np.sin(i * np.pi / 180) * np.cos(j * np.pi / 180)
            circulation_pattern[i, j] = energy_level

    return circulation_pattern

# Call the function
circulation_pattern = simulate_energy_circulation()
print(circulation_pattern)

