from celery import Celery
from redis import StrictRedis
import time

app = Celery('tasks')

r = None

@app.task
def no_op():
    global r
    if r is None:
        r = StrictRedis(host=host, port=port, db=db)
    i = r.decr("countdown")
    if i == 0:
        r.set("finish", time.time())

@app.task
def enqueue(host,port,db,n):
    global r
    if r is None:
        r = StrictRedis(host=host, port=port, db=db)
    r.set("start", time.time())
    r.set("countdown", n)
    for i in range(n):
        no_op.s().apply_async()
    
