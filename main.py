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

# Print config properties
print(use_discord_bot)
print(use_discord_debug_mode)
print(fortnite_account_id)
print(fortnite_device_id)
print(fortnite_secret)
print(gift_to_accounts)
print(f"Developer Settings JSON: {dev_settings}")