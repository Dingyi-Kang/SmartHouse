import smbus
import time
import socket
import pymongo
from pymongo import MongoClient
sensor = MongoClient('localhost')
print (sensor)
db = sensor.values
db.values.count()
values = db.values
values.find()



bus = smbus.SMBus(1)



while True:
    bus.write_byte(0x48, 0x84)
    time.sleep(0.3)
    data = bus.read_byte(0x48)
    values = db.values.insert({"WindSensorVal":data});
    print "Digital value of analog input is: %d" %data

