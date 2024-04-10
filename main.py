import requests
import json
from json import *
config = None
with open('config.json') as config_file:
    config = json.load(config_file)

useDiscordbot = config.discord.useDiscordBot
useDiscordDebugMode = config.discord.dbg
fortniteAccountID = config.auth.accountId
fortniteDeviceID = config.auth.deviceId
fortniteSecret = config.auth.secret
giftToAccounds = config.giftToInfo.accounts
devSettings = config.developerSettings

print(useDiscordBot)
print(useDiscordDebugMode)
print(fortniteAccountID)
print(fortniteDeviceID)
print(fortniteSecret)
print(giftToAccounds)
print(f"Developer Settings JSON: {developerSettings}")