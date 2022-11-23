from datetime import datetime
import random 
import time

while True:
    microsec = datetime.now().microsecond
    if microsec in range(0,30):
        time.sleep(random.randint(1, 10))
        print(datetime.now())