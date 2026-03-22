from multiprocessing import Process
import time

def background_task():
    print("Processing started...")
    time.sleep(5)
    print("Processing done!")

if __name__ == "__main__":
    p = Process(target=background_task)
    p.start()

    print("Main app continues...")