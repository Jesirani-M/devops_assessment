import time
from datetime import datetime
 
FILE_PATH = "/app/data/log.txt"
 
while True:
    with open(FILE_PATH, "a") as f:
        f.write(f"Log entry at {datetime.now()}\n")
    print("Appended a new line")
    time.sleep(5)
