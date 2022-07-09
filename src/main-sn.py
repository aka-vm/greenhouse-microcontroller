from sensors.dht11 import DHT11
from time import sleep

sensor = DHT11(pin=4)
delay_time = 10

while True:
    data = sensor.read()
    send_data(data)
    sleep(delay_time)
    print("Sleeping for {} seconds".format(delay_time))
    print("\n")
