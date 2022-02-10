import time

class timer:
    def __init__(self):
        self.start = 0
        self.end = 0 
        self.result = 0

    def start(self):
        self.start = time.time()
        #print("start timer by lh-tintylib")

    def stop(self):
        self.end = time.time()
        #print("stop timer by lh-tintylib")
        self.result = self.end - self.start
        return self.result
        
    def simple_print(self):
        print("simple ok")
        

