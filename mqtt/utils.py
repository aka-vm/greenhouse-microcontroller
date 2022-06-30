import json

def get_broaker_url():
    with open("mqtt-config.json") as f:
        config = json.load(f)
    link = config["broaker_link"]
    port = config["broaker_port"]

    return link+":"+port
