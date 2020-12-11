"""
Registering Slash Command
"""
import requests
from config import token # Token of Bot

url = "https://discord.com/api/v8/applications/653534001742741552/guilds/653083797763522580/commands" # for guild

thanks = {
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

cat = {
  "name": "고양이",
  "description": "귀여운 고양이 사진을 보냅니다냥~!",
  "options": [
    {
      "name": "사진크기",
      "description": "사진의 사진 크기입니다.",
      "type": 3,
      "required": True,
      "choices": [
        {
          "value": "small",
          "name": "작은 사진이다냥.."
        },
        {
          "value": "medium",
          "name": "중간 사진이다냥.."
        },
        {
          "value": "original",
          "name": "크게 크게 크게!!! 다냥.."
        }
      ]
    }
  ]
}
json = cat

# For authorization, you can use either your bot token 
headers = {
    "Authorization": f"Bot {token}"
}

r = requests.post(url, headers=headers, json=json)

print(r.json())