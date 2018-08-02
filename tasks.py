from celery import Celery

app = Celery('tasks')

@app.task
def no_op():
    pass

@app.task
def enqueue(n):
    for i in range(n):
        no_op.s().apply_async()
    
