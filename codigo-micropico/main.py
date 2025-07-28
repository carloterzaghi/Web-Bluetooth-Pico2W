from machine import Pin
import bluetooth
from ble_simple_peripheral import BLESimplePeripheral
from ble_advertising import advertising_payload

# Inicializa BLE e perfil
ble = bluetooth.BLE()
# Nome do dispositivo que será anunciado
sp = BLESimplePeripheral(ble, name="Pico2W")

# LED onboard
led = Pin("LED", Pin.OUT)
led_state = False

def on_rx(data):
    global led_state
    cmd = data.decode('utf-8').strip().lower()
    print("Recebido:", cmd)
    if cmd in ("on","1","true"):
        led.value(1)
        led_state = True
    elif cmd in ("off","0","false"):
        led.value(0)
        led_state = False
    elif cmd in ("toggle", "tg"):
        led.toggle()
        led_state = not led_state

# Loop principal aguarda conexão
while True:
    if sp.is_connected():
        sp.on_write(on_rx)
