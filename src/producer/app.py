import time
from celery import Celery

app = Celery('producer', broker='redis://redis:6379/0')

@app.task
def add(x, y):
    return x + y

if __name__ == '__main__':
    while 1:
        for i in range(10):
            add.delay(i, i + 1)
        time.sleep(10)
