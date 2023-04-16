import requests
import time
import os

url = "YOUR ONLINE CAMERA LINK LIKE: http://128.65.187.44:85/webcapture.jpg?command=snap&channel=7?1681636203"
directory = "images"

if not os.path.exists(directory):
    os.makedirs(directory)

i = 0
while True:
    response = requests.get(url)

    filename = f"{directory}/image_{i}.jpg"
    while os.path.exists(filename):
        i += 1
        filename = f"{directory}/image_{i}.jpg"

    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Image saved: {filename}")
    i += 1
    time.sleep(2)
