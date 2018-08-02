from benchmarkutils import enqueue
import sys

n = int(sys.argv[1])

enqueue.s(n).apply_async()
