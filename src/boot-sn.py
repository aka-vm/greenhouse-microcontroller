from wifi import wifi_client
import gc
import json
from umqtt.simple import MQTTClient

def send_data(data):

    import urequests
    t_id = 1
    h_id = 2
    print("Sending data:")

    host = get_host()
    endpoint = host + "/api/sensor/{}/"

    # format id
    t_data = {
        "id": t_id,
        "type": "temprature",
        "value": data[0]
    }
    print("Temperature data sending {}".format(t_data))
    r1 = urequests.put(endpoint.format(t_id), json=json.dumps(t_data))

    h_data = {
        "id": h_id,
        "type": "humidity",
        "value": data[1]
    }
    print("Humidity data sending {}".format(h_data))
    r2 = urequests.put(endpoint.format(h_id), json=json.dumps(h_data))

    print(r1.json())
    print(r2.json())


def get_host():
    with open("main-config.json") as f:
        host = json.load(f)["host-addr"]

    return "http://"+host


wifi_client.connect()



gc.collect()
