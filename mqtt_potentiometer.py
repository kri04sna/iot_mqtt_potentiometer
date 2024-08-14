import network
import time
from machine import Pin, ADC
import ujson
from umqtt.simple import MQTTClient

# MQTT Server Parameters
MQTT_CLIENT_ID = "micropython-potentiometer-demo"
MQTT_BROKER    = "broker.mqttdashboard.com"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
MQTT_TOPIC     = "wokwi-potentiometer"

# Potentiometer configuration
potentiometer = ADC(Pin(34))  # Connect to ADC pin 34
potentiometer.atten(ADC.ATTN_11DB)  # Set the attenuation for full 0-3.3V range

print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
    print(".", end="")
    time.sleep(0.1)
print(" Connected!")

print("Connecting to MQTT server... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
client.connect()

print("Connected!")

prev_value = None
while True:
    pot_value = potentiometer.read()  # Read the potentiometer value
    if pot_value != prev_value:
        message = ujson.dumps({"potentiometer": pot_value})
        print(f"Potentiometer value: {pot_value}")
        print(f"Reporting to MQTT topic {MQTT_TOPIC}: {message}")
        client.publish(MQTT_TOPIC, message)
        prev_value = pot_value
    time.sleep(0.5)
