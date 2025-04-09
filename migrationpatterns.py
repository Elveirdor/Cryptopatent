import matplotlib.pyplot as plt

# Define the migration data
migration_data = {
    'Country A': {'Country B': 100, 'Country C': 50},
    'Country B': {'Country A': 20, 'Country C': 30},
    'Country C': {'Country A': 10, 'Country B': 40}
}

# Create a figure and axis
fig, ax = plt.subplots()

# Set the title and labels
ax.set_title('Migration Chart')
ax.set_xlabel('Destination Country')
ax.set_ylabel('Number of Migrants')

# Create bars for each country
for i, (country, destinations) in enumerate(migration_data.items()):
    for j, (destination, migrants) in enumerate(destinations.items()):
        ax.bar(i + j * 0.1, migrants, width=0.1, label=f'{country} to {destination}')

# Add a legend
ax.legend()

# Show the plot
plt.show()
