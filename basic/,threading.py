import threading, time

def prints(name, sleep_time):
    for i in range(10):
        print(name + ': ' + str(i))
        time.sleep(sleep_time)

thread1 = threading.Thread(target=prints, args=('A', 1,))  # Initialize
thread2 = threading.Thread(target=prints, args=('B', 1,))
thread1.start() # Start
thread1.join()  # WAIT HERE
thread2.start()
