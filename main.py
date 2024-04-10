import requests
import json
from json import *
config = None
with open('config.json') as config_file:
    config = json.load(config_file)

print(config)