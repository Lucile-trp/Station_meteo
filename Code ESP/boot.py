# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine, time, network
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()

#connexion à internet
def connectToInternet():
    #import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connexion au réseau...')
        wlan.connect('MI 9', 'chounette')
        #wlan.connect('Julien-IOT', '')
        while not wlan.isconnected():
            pass
    print('Connecté à l\'internet')
connectToInternet()

import si7021
from machine import I2C, Pin

i2c = I2C(-1, Pin(2), Pin(0))
s = si7021.SI7021(i2c)

temp_avg = []
hum_avg = []

while True:
    from time import sleep_ms, ticks_ms
    
#Récupération des données depuis la sonde      
    temp = s.temperature()
    humidity = s.humidity()

    data = {'temperature':temp, 'humidity':humidity}
    
#Moyenne des 5 derniers relevé
    temp_avg = []
    while len(temp_avg) < 10:
        temp = s.temperature()
        temp_avg.append(temp)
        time.sleep(720)
        
    print("liste crée :",temp_avg)
    temp_avg = sum(temp_avg) / len(temp_avg)
    print("moy temp:",temp_avg)
    
    hum_avg = []
    while len(hum_avg) < 10:
        humidity = s.humidity()
        hum_avg.append(humidity)
        time.sleep(720)
        
    print("liste crée :",hum_avg)    
    hum_avg = sum(hum_avg) / len(hum_avg)
    print("moy hum: ",hum_avg)
    
    data = {'temperature':temp_avg, 'humidity':hum_avg}
    
#Envoi des données à l'API    
    import urequests
    import json
    
    #IP Lucile
    #url = "http://192.168.43.135:5000/api/v1/mesure/add"
    url = "http://192.168.43.60:5000/api/v1/mesure/add"
    
    print ("Envoi des données vers :",url)
    
    r = urequests.post(url, json=data)
    print("Status de la requête POST: ",r.status_code)
    time.sleep(3600)
    
    del(temp_avg)
    del(hum_avg)