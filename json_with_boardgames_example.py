
# This Python script demonstrates JSON serialization and deserialization
# with a custom Python class called 'BoardGame'.
# It shows how to store objects as JSON, then load and reconstruct them.
#
# JSON is useful for saving structured data to files or transferring it over networks.
# This example helps understand how Python objects can be translated to JSON and vice versa.
# ----------------------------------------

import json  # Importing the json module

# ------------------------------
# 1. BASIC DICTIONARY SERIALIZATION
# ------------------------------

# A simple user profile dictionary
user_profile = {
    "username": "boardlover92",
    "email": "gamer@example.com",
    "member_since": 2020,
    "favorites": ["strategy", "co-op", "card games"]
}

# Convert the dictionary to a JSON string
json_string = json.dumps(user_profile)
print("Serialized user profile to JSON string:")
print(json_string)

# Save the user profile to a file
with open("user_profile.json", "w") as file:
    json.dump(user_profile, file)
    print("User profile saved to 'user_profile.json'")

# ------------------------------
# 2. CUSTOM CLASS: BoardGame
# ------------------------------

# Define a custom class called BoardGame
class BoardGame:
    def __init__(self, game_id, name, min_players, max_players, price):
        self.game_id = game_id
        self.name = name
        self.min_players = min_players
        self.max_players = max_players
        self.price = price

# Create instances of BoardGame
g1 = BoardGame(101, "Catan", 3, 4, 45.99)
g2 = BoardGame(102, "Pandemic", 2, 4, 39.50)

# Serialize objects to dictionary format using __dict__
games_data = {
    g1.game_id: g1.__dict__,
    g2.game_id: g2.__dict__
}

# Save to a JSON file
with open("boardgames.json", "w") as file:
    json.dump(games_data, file)
    print("Board games saved to 'boardgames.json'")

# ------------------------------
# 3. DESERIALIZATION AND OBJECT RECONSTRUCTION
# ------------------------------

# Load the JSON file
with open("boardgames.json", "r") as file:
    loaded_games = json.load(file)
    print("Board games loaded from 'boardgames.json'")

# Reconstruct BoardGame objects from JSON
game_list = []
for key, value in loaded_games.items():
    game = BoardGame(
        int(key),
        value["name"],
        value["min_players"],
        value["max_players"],
        value["price"]
    )
    game_list.append(game)

# Print out the deserialized game objects
print("Deserialized BoardGame objects:")
for game in game_list:
    print(f"{game.name} ({game.min_players}-{game.max_players} players): ${game.price}")

# ------------------------------
# End of Script
# ------------------------------
