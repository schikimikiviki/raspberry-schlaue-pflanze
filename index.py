import RPi.GPIO as gpio
import dht11
import spidev
import time
import os

# LED
led = 21
gpio.setmode(gpio.BCM)
gpio.setup(led, gpio.OUT)

# DHT11
sensor = dht11.DHT11(pin=4)

# SPI Verbindung herstellen
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

# Liest Daten vom MCP3008
def analogEingang(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

def pflanze_messen():
  helligkeit = analogEingang(0)
  bodenFeuchtigkeit = analogEingang(1)

  if bodenFeuchtigkeit > 650:
    print("Du solltest deine Pflanze Waessern")
    gpio.output(led, gpio.HIGH)
  else:
    gpio.output(led, gpio.LOW)

  print("===========================")
  print("Feuchtigkeit: "+str(bodenFeuchtigkeit))
  print("Helligkeit: "+str(helligkeit))

  result = sensor.read()
  if result.is_valid()
    print("Temperatur: "+str(result.temperature))
    print("Feuchtigkeit: "+str(result.humidity)+"%")
  time.sleep(1.2)

pflanze_messen()
