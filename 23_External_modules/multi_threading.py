import time
import threading

def loading(num):
    print(f"Thread {num}: Starting")
    time.sleep(2)
    print(f"Thread {num}: Ending")


threads = []
for i in range(3):
    thread = threading.Thread(target=loading,args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All threads are completed")
