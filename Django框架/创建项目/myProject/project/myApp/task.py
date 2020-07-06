import time
from celery import task

@task
def func():
    time.sleep(5)
    print("hanyb is good man")
    time.sleep(5)
    print("hanyb is good man")