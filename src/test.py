import json
import requests

# host = "http://localhost:8000"
# endpoint = host + "/api/sensor/2/"
# h_id = 2
# h_data = {
#         "id": h_id,
#         "type": "humidity",
#         "value": 85
#     }

# r = requests.put(endpoint.format(h_id), data=h_data)
# print(r.json())

def get_host():
    host = "192.168.31.162:8000"

    return "http://"+host

def send_data(data):
    import urequests

    t_id = 1
    h_id = 2

    t_data = {
        "id": t_id,
        "type": "temprature",
        "value": data[0]
    }
    h_data = {
        "id": h_id,
        "type": "humidity",
        "value": data[1]
    }
    print("Sending data:")

    host = get_host()
    endpoint = host + "/api/sensor/{}/"

    # format id
    requests.put(endpoint.format(t_id), data=t_data)
    print("Temperature data sent {}".format(t_data))
    requests.put(endpoint.format(h_id), json=h_data)
    print("Humidity data sent {}".format(h_data))


send_data([25, 85])

