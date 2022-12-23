from playsound import playsound
import time
from forex_python.converter import CurrencyRates

cr = CurrencyRates()
mem = cr.get_rate("USD", "TRY")

while True:
    current = cr.get_rate("USD", "TRY")
    print(current)

    if current > mem:
        print("Yetherrrrrrrrrrrr")
        playsound("yeter.mp3")

    time.sleep(120)
