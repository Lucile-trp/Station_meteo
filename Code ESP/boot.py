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
import si7021
from machine import I2C, Pin

i2c = I2C(-1, Pin(2), Pin(0))
s = si7021.SI7021(i2c)

i = 0

while i < 10:
    from time import sleep_ms, ticks_ms
    from machine import I2C, Pin
    from esp8266_i2c_lcd import I2cLcd

    i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)

    lcd = I2cLcd(i2c, 0x27, 2, 16)
    lcd.putstr("Hello ernitron\nIt's working!")
    lcd.clear()
    lcd.putstr("Using dhylands\npython_lcd")

    lcd = I2cLcd(i2c, 0x27, 4, 20)
    lcd.putstr("WeMos D1 Mini with  PCF8574 I2C backpackWorks with HD44780s:08x2 16x1 16x2 20x4")
    lcd.clear()
    lcd.putstr("line 1\nline 2\nline 3\nline 4")
    temp = s.temperature()
    humidity = s.humidity()

    data = {'temperature':temp, 'humidity':humidity}

    import urequests
    import json
    
    url = "http://192.168.43.135:5000/api/v1/mesure/add"

    print(data)
    r = urequests.post(url, json=data)
    print(r.status_code)
    import time
    time.sleep(5)
    
    i += 1