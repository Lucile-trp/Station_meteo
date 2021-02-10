# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()

#connexion à internet
def connectToInternet():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connexion au réseau de Mariam...')
        wlan.connect('MI 9', 'chounette')
        while not wlan.isconnected():
            pass
    print('Connecté à l\'internet')
connectToInternet()

i = 0

while i < 10:
    import si7021
    from machine import I2C, Pin

    i2c = I2C(-1, Pin(2), Pin(0))
    s = si7021.SI7021(i2c)

    temp = s.temperature()
    humidity = s.humidity()

    data = [temp,humidity]

    import urequests
    import json
    
    data = json.dumps(data)
    url = "http://192.168.43.135:5000/api/v1/mesure/add"
    urequests.post(url,data)
    
    import time
    time.sleep(5)
    
    i += 1