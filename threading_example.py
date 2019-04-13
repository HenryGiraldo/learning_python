#!/usr/bin/env python3

#Original idea from Reuven Lerner in:
#https://www.linuxjournal.com/content/threading-python

from queue import Queue
import threading
import requests
import time

def get_length(url):
    try:
        response = requests.get(url)
        queue.put((one_url, len(response.content)))
    except:
        print("Skipping ", url, ", can't establish connection")

queue = Queue()
length = {}
threads = []

try:
    urls = [one_line.strip() for one_line in open('urls.txt')]
except:
    print("define a file named urls.txt file which contains valid urls")
    quit()

print("Getting content")
start_time = time.time()
for one_url in urls:
    t = threading.Thread(target=get_length, args=(one_url,))
    threads.append(t)
    t.start()

print("Joining threads")
for one_thread in threads:
    one_thread.join()

for key, value in length.items():
    print("{0:30}: {1:8}".format(key,value))

end_time = time.time()

total_time = end_time - start_time

print("\nTotal time: {0:.3} seconds".format(total_time))
