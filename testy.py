import time
import os
import pandas

while True:
    if os.path.exists("files/vegetables.txt"):
        with open("files/vegetables.txt") as file:
            print(file.read())
    else:
        print("Soubor neexistuje")

    time.sleep(10)