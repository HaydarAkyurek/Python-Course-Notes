# This Python script demonstrates how to make a GET request to a public API using RapidAPI.
# Specifically, it fetches a random joke from the "JokeAPI" available on RapidAPI.
#
# RapidAPI is a popular API marketplace where developers can discover and connect to thousands of APIs.
# You can access JokeAPI by visiting: https://rapidapi.com/Spott/api/jokeapi-v2/
#
# Purpose:
# Learn how to:
# - Connect to a third-party API
# - Set up request headers including API keys
# - Handle JSON responses
# - Extract and print meaningful data (jokes in this case)
# -------------------------------

import requests  # Import the requests library to make HTTP requests
import json      # Import json to handle JSON responses

# Define the API endpoint from JokeAPI (on RapidAPI)
url = "https://jokeapi-v2.p.rapidapi.com/joke/Any"

# Define the query parameters
# 'format' sets the response type, and 'safe-mode' ensures no offensive content
querystring = {
    "format": "json",
    "blacklistFlags": "nsfw,religious,political,racist,sexist,explicit",
    "safe-mode": "true"
}

# Set the required headers including the RapidAPI key and host
headers = {
    "X-RapidAPI-Key": "YOUR_RAPIDAPI_KEY_HERE",  # Replace with your actual RapidAPI key
    "X-RapidAPI-Host": "jokeapi-v2.p.rapidapi.com"
}

# Send a GET request to the API with headers and parameters
response = requests.get(url, headers=headers, params=querystring)

# Check if the request was successful (status code 200 means OK)
if response.status_code == 200:
    print("Request successful!")
    
    # Convert the JSON response to a Python dictionary
    data = response.json()

    # Check if the joke is a 'single' type or a 'two-part' type
    if data["type"] == "single":
        # Print the joke directly
        print("\nHere's a random joke for you:")
        print(data["joke"])
    elif data["type"] == "twopart":
        # Print the setup and delivery separately
        print("\nHere's a random joke for you:")
        print("Setup:", data["setup"])
        print("Punchline:", data["delivery"])
    else:
        print("Unexpected joke format.")
else:
    # If the request failed, print the error message
    print(f"Request failed with status code {response.status_code}")
    print("Reason:", response.text)
