import random
import time

# Infinite run sensor until pipeline timeout forced
def run_sensor(): 
    while True:
        voltage = round(random.uniform(0.0, 5.0), 2) # Random Voltage
        print(f"Voltage reading: {voltage} V")
        time.sleep(1) # Repeat after wait

print("Weather Station Sensor started...") # Confirms start

# Infinite Checker
while True: 
    try:
        run_sensor()
    except Exception as e: # Catch Failure and let operator know
        print("Sensor failure detected. Restarting sensor...")
        time.sleep(2) # Attempt to restart Sensor
