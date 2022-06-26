import dht
from machine import Pin

class DHT11:
    def __init__(self, pin):
        self.pin = pin
        self.dht11 = dht.DHT11(Pin(pin))

    def read(self):
        """
        outputs a tuple of (temperature, humidity)
        """
        self.dht11.measure()
        return self.dht11.temperature(), self.dht11.humidity()