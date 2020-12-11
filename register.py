"""
Registering Slash Command
"""
import requests


url = "https://discord.com/api/v8/applications/653534001742741552/guilds/653083797763522580/commands" # for guild

json = {
    "name": "thanks",
    "description": "감사를 표합니다.",
    "options": [
        {
            "name": "감사를표할분",
            "description": "감사하신 분께 자신의 마음을 표현해보세요,",
            "type": 6,
            "required": True
        }
    ]
}

# For authorization, you can use either your bot token 
headers = {
    "Authorization": "Bot SuperSecretToken"
}

r = requests.post(url, headers=headers, json=json)

print(r.json())