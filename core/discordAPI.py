import requests
from PyJS import JSON
from PyJS.modules import fs

settings = JSON.parse(fs.createReadStream('settings.json'))

params = {
    "headers":{
        "Authorization": "Bot " + settings['bot_token'],
        "Content-Type": "application/json"
    }
}

def get_guild(guild_id):
    return requests.get("https://discord.com/api/guilds/" + str(guild_id) + "?with_counts=true", **params).json()

def get_invite(channel_id):
    data = {
        "max_age": 0,
        "max_uses": 0,
        "unique": False
    }
    return requests.post("https://discord.com/api/channels/" + str(channel_id) + "/invites", json=data, **params)