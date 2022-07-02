from wifi import wifi_client
import gc
from machine import Pin

heater = Pin(4, Pin.OUT)
humidifier = Pin(0, Pin.OUT)

def get_host():
    import json
    with open("main-config.json") as f:
        host = json.load(f)["host-addr"]

    return "http://"+host

def request_data():
    import urequests
    t_id = 1
    h_id = 2

    print("Requesting Sensor data:")
    host = get_host()
    endpoint = host + "/api/sensor/{}/"

    t_data = urequests.get(endpoint.format(t_id)).json()
    h_data = urequests.get(endpoint.format(h_id)).json()

    print(t_data)
    print(h_data)

    return [t_data["value"], h_data["value"]]

wifi_client.connect()

gc.collect()
