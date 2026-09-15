# Project 3: AI Recommendation Logic

items = {
    "Avengers": ["action", "adventure", "superhero"],
    "Interstellar": ["sci-fi", "adventure", "space"],
    "Titanic": ["romance", "drama"],
    "The Conjuring": ["horror", "thriller"],
    "Inception": ["sci-fi", "action", "thriller"],
    "The Notebook": ["romance", "drama"],
    "Jumanji": ["adventure", "comedy", "action"],
    "Insidious": ["horror", "thriller"],
    "Spider-Man": ["action", "adventure", "superhero"],
    "Frozen": ["animation", "adventure", "comedy"]
}

print("==========================================")
print("       AI RECOMMENDATION SYSTEM")
print("==========================================")

print("\nAvailable Interests:")
print("action, adventure, superhero")
print("sci-fi, space, romance, drama")
print("horror, thriller, comedy, animation")

# Get user input
user_input = input("\nEnter your interests: ")

# Convert input into list
preferences = user_input.lower().split(",")

recommendations = []

# Match user preferences
for item, categories in items.items():

    score = 0

    for preference in preferences:
        preference = preference.strip()

        if preference in categories:
            score = score + 1

    if score > 0:
        recommendations.append((item, score))

# Sort by highest score
recommendations.sort(key=lambda x: x[1], reverse=True)

# Display results
print("\n==========================================")
print("          RECOMMENDED ITEMS")
print("==========================================")

if len(recommendations) > 0:

    for item, score in recommendations:

        percentage = (score / len(preferences)) * 100

        print("\nItem:", item)
        print("Matched Preferences:", score)
        print("Similarity:", round(percentage, 2), "%")

else:
    print("\nNo matching recommendations found.")

print("\n==========================================")
print(" Thank you for using the AI Recommendation System!")
print("==========================================")