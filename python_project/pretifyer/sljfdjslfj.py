import requests
import json
query="hello"
response = requests.get(
            f"https://nekobot.xyz/api/")
data = json.loads(response.text)
# print(data['translated'])
print(data)