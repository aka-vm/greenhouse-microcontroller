# Micropython ESP32/8266 WiFi module

from machine import Pin, SPI
import network
import time
import json

def load_configs():
    with open('wifi-configs.json') as f:
        return json.load(f)

def connect_wifi(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(ssid, password)
        for i in range(0, 10):
            print('.', end='')
            time.sleep(1)
            if sta_if.isconnected():
                print()
                return True
        return False
    else:
        return True

def connect():
    wifi_config_list = load_configs()
    for wifi_config in wifi_config_list:
        ssid = wifi_config['ssid']
        password = wifi_config['password']
        print('Connecting to {}...'.format(ssid))
        is_connected = connect_wifi(ssid, password)
        if is_connected:
            print('Connected to {}'.format(ssid))

            gc.collect()
            return True
        print('Failed to connect to {}'.format(ssid))

    print("No WiFi connection available")

    return False

def disconnect():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.disconnect()
    sta_if.active(False)
