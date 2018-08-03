from tasks import enqueue
from redis import StrictRedis
import sys
import time

host = sys.argv[1]
port = int(sys.argv[2])
db = int(sys.argv[3])
n = int(sys.argv[4])

r = StrictRedis(host=host, port=port, db=db)
r.delete("start")
r.delete("finish")
r.delete("countdown")
enqueue.s(host, port, db, n).apply_async()

while r.get("finish") is None:
    time.sleep(1)

start = float(r.get("start"))
finish = float(r.get("finish"))

print(finish-start)




