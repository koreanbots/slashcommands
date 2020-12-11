import requests
from config import token # Token of Bot

url = "https://discord.com/api/v8/applications/653534001742741552/guilds/653083797763522580/commands/786838974769266688" # for guild

# For authorization, you can use either your bot token 
headers = {
    "Authorization": f"Bot {token}"
}

r = requests.delete(url, headers=headers)

print(r.status_code)