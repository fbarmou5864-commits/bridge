import requests
import random
import time

SERVER = "http://10.135.4.13:5000/"

n= input("Enter your name")

temperature = round(random.uniform(18, 30), 1)
  
payload = {
    "name": n,
    "role": "Example Sensor",
    "message": f"Current Temperature: {temperature}°C"
}

requests.post(SERVER, data=payload)

print("Sent:", temperature)