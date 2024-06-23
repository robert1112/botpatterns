import requests
import json

# Fetch the list of bots
url = "https://raw.githubusercontent.com/monperrus/crawler-user-agents/master/crawler-user-agents.json"
response = requests.get(url)
bots_data = response.json()

# Extract the user agent patterns
user_agents = [entry['pattern'] for entry in bots_data]

# Save the list to a file
with open('bot_list.json', 'w') as f:
    json.dump(user_agents, f)

print("Bot list updated successfully.")
