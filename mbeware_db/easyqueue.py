#pip install "persist-queue[async]"

#How to use
# from persistqueue import FIFOSQLiteQueue
# from threading import Thread

# q = FIFOSQLiteQueue(path="./test", multithreading=True)

# def worker():
#     while True:
#         item = q.get()
#         do_work(item)

# for i in range(num_worker_threads):
#      t = Thread(target=worker)
#      t.daemon = True
#      t.start()

# for item in source():
#     q.put(item)



