import settings
import requests
import json
from json import *

# Load config from config.json
with open('config.json') as config_file:
    config = json.load(config_file)

# Access config properties
use_discord_bot = config["discord"]["useDiscordBot"]
use_discord_debug_mode = config["discord"]["dbg"]
fortnite_account_id = config["auth"]["accountId"]
fortnite_device_id = config["auth"]["deviceId"]
fortnite_secret = config["auth"]["secret"]
gift_to_accounts = config["giftToInfo"]["accounts"]
dev_settings = config["developerSettings"]


def login(accid, devid, secret):
    url = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "basic UHl0aG9uLXVzZXI6IG5pY2V9CnN0YW5kYXJkUHJvZmVzZXI6IEVsZW1lbnQgZ3JvdmU9ICJmZmQ0ODlmYy04ZWZkLWNmY2QtYmYwYS0wZmE1Y2Q3M2NhZmEiOw==",
        "X-Epic-Device-ID": "1aadad8asd"
    }

    body = {
        "grant_type": f"device_auth&accountId={fortnite_account_id}&deviceId={fortnite_device_id}&secret={fortnite_secret}"
    }

    response = requests.post(url, headers=headers, data=json.dumps(body))
``    print(response)