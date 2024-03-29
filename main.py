import time
from datetime import datetime
import os
import Adafruit_DHT
from bmp280 import BMP280
from smbus2 import SMBus
from influxdb import InfluxDBClient
from dotenv import load_dotenv
load_dotenv()


pin_1 = 17 #innen
pin_2 = 22 #außen
bus = SMBus(1)


#import from .env File
USER = os.environ.get('USER')
PASSWORT = os.environ.get('PASSWORD')
HOST = os.environ.get('HOST')

#handover sensor parameter in a variable
sensor_dht = Adafruit_DHT.DHT22
sensor_bmp = BMP280(i2c_dev=bus)


#endless loop for data collection and writting in the influxdb
while True:
    #read sensor data
    hum_1, temp_1 = Adafruit_DHT.read_retry(sensor_dht, pin_1)
    hum_2, temp_2 = Adafruit_DHT.read_retry(sensor_dht, pin_2)
    preassure = sensor_bmp.get_pressure()
    
    #data to variable
    timestamp = datetime.now()
    hum_1 = round(hum_1, 1)
    temp_1 = round(temp_1, 1)
    hum_2 = round(hum_2, 1)
    temp_2 = round(temp_2, 1)
    preassure = int(preassure)
    
    #define post request into influxdb
    client = InfluxDBClient(HOST, 4000, USER, PASSWORT, 'wetterstation')

    
    json_payload = []
    data_1 = {
        'measurement' : 'wetterdaten',
        'tags' : {
            'ort' : 'innen'
        },
        'time' : timestamp,
        'fields' : {
            'Temperatur' : temp_1,
            'Luftfeuchtigkeit' : hum_1
        }
    }
    data_2 = {
        'measurement' : 'wetterdaten',
        'tags' : {
            'ort' : 'außen'
        },
        'time' : timestamp,
        'fields' : {
            'Temperatur' : temp_2,
            'Luftfeuchtigkeit' : hum_2,
            'Luftdruck' : preassure
        }
    }
    
    json_payload.append(data_1)
    json_payload.append(data_2)
    
    client.write_points(json_payload)
    
    # print(F'T-1 {temp_1}°C', F'F-1 {hum_1}%', F'T-2 {temp_2}°C', F'F-2 {hum_2}%', F'D {preassure}hPa', F'{timestamp}')
    time.sleep(5)
