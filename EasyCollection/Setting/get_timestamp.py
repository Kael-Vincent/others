import time

def get_timestamp():
    t = time.time()
    timestamp = str(round(t * 1000))
    print(timestamp)
    return timestamp
get_timestamp()

