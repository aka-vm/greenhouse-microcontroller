import time

check_time = 10

t_cap = 28
h_cap = 70

while True:
    data = request_data()
    t = data[0]
    h = data[1]

    if t > t_cap:
        print("Heater OFF")
        heater.off()
    else:
        print("Heater ON")
        heater.on()

    if h > h_cap:
        print("Humidifier OFF")
        humidifier.off()
    else:
        print("Humidifier ON")
        humidifier.on()

    time.sleep(5)
