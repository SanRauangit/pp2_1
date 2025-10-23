import math
import time
def delay_sqrt(a,delay_ms):
    time.sleep(delay_ms/1000.0)
    result=math.sqrt(a)
    print(f"Square root of {a} after {delay_ms} miliseconds is {result}")
num=int(input())
sec=int(input())
r=delay_sqrt(num,sec)