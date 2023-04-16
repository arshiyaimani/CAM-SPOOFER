import requests
import time
import os

links = ["http://5.201.187.32:8080/webcapture.jpg?command=snap&channel=1?6", "http://5.201.187.32:8080/webcapture.jpg?command=snap&channel=2?6", "http://5.201.187.32:8080/webcapture.jpg?command=snap&channel=3?6" , "http://5.201.187.32:8080/webcapture.jpg?command=snap&channel=4?6" , "http://5.201.187.32:8080/webcapture.jpg?command=snap&channel=5?6" , "http://5.201.187.32:8080/webcapture.jpg?command=snap&channel=6?6" , "http://5.201.187.32:8080/webcapture.jpg?command=snap&channel=7?6" , "http://5.201.187.32:8080/webcapture.jpg?command=snap&channel=8?6" ]
directory = "images"

if not os.path.exists(directory):
    os.makedirs(directory)

i = 0
while True:
    response = requests.get(links[i % len(links)])

    filename = f"{directory}/image_{i}.jpg"
    while os.path.exists(filename):
        i += 1
        filename = f"{directory}/image_{i}.jpg"

    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Image saved: {filename}")
    i += 1
    if i == 8:
        i = 0   # Reset the index to start over with the first link
    time.sleep(2)
