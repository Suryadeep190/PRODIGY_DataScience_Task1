import matplotlib.pyplot as plt

# Sample data
labels = ['Male', 'Female', 'Non-Binary', 'Prefer not to say']
counts = [450, 500, 75, 25]  # Example counts for each category

# Plotting
plt.figure(figsize=(8, 6))
plt.bar(labels, counts, color=['blue', 'pink', 'purple', 'gray'])
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Distribution of Gender in the Population')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()
