from umqtt.simple import MQTTClient
import json

def get_broaker_url():
    with open("mqtt-config.json") as f:
        config = json.load(f)
    link = config["broaker_link"]
    port = config["broaker_port"]

    return link+":"+port

class Subscriber:
    broaker_url = get_broaker_url()

    def __init__(self, topic):
        client = MQTTClient(topic, self.broaker_url)
        client.set_callback(topic)
        client.connect()

        self.client = client



    def callback(self, topic, msg):
        print(topic, msg)
        return topic, msg