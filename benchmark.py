from celery import Celery
import sys

broker_url = sys.argv[1]
n = int(sys.argv[2])

app = Celery('tasks', broker=broker_url)

@app.task
def no_op():
    pass

@app.task
def enqueue(n):
    for i in range(n):
        no_op.s().apply_async()
    
enqueue.s(n).apply_async()
