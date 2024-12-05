import time
import random
from celery import Celery

app = Celery('tasks', broker='redis://redis:6379/0')

@app.task(name="producer.add")
def add(x, y):
    t = random.randint(1, 10)
    print(f"Sleeping for {t} seconds")
    time.sleep(t)
    return x + y
