import http.client
import json
from telegram_push import post_message

conn = http.client.HTTPSConnection("tiktok-api23.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "",
    'x-rapidapi-host': "tiktok-api23.p.rapidapi.com"
}

try: 
    conn.request("GET", "/api/user/info?uniqueId=jak.coin", headers=headers)

    res = conn.getresponse()
    data = res.read()

    data = json.loads(data.decode("utf-8"))

    followers = data['userInfo']['stats']['followerCount']

    message = f"Jak Follower count = {followers}"

    post_message(message)

except Exception as e:
    message = f"error : {e}"
    post_message(message)