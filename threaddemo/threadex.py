import threading

import time

def sleeper(n, name):
    print ("Hi I am {}. Going sleep for 5 sec".format(name))
    time.sleep(n)
    print ("{} has waken from sleep".format(name))

# t = threading.Thread(target=sleeper, name="thread1", args= (5,"thraed1"))
# t.start()

threadlist = []

start = time.time()
for i in range(5):
    t = threading.Thread(target=sleeper, name="thread{}".format(i), args=(5, "thread{}".format(i)))
    threadlist.append(t)
    t.start()
    print ("{} has started".format(t.name))

for t in threadlist:
    t.join()

end=time.time()

print ("time taken {}".format(end-start))

print ("All threads finished their job")