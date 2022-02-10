import lhtinylib
import time
from time import sleep

lh = lhtinylib.timer()

lh.start
sleep(0.5)
rtn = lh.stop()
print(rtn)

lh.simple_print()

