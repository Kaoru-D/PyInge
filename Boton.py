import paho.mqtt.client as mqtt
import time
from pymodbus.client import ModbusTcpClient

PLC= ModbusTcpClient("192.168.0.20")
PLC.connect()

servidor= "broker.mqtt.cool"
cliente=mqtt.Client(protocol=mqtt.MQTTv5)

cliente.connect(servidor,1883)

try:
    while True:
        lectura =PLC.read_discrete_inputs(0,1)
        estadoEntrada= lectura.bits[0]
        cliente.publish("DanielPLC", estadoEntrada)
        time.sleep(0.5)
except:
    PLC.close()