""""test commit & push w/ manjaro linux
"""
import time
import sys

print ("All App's and extensions work well.")
time.sleep(1)
print ("Power off")
time.sleep(1)
for _ in range(3,0,-1):
    print("Turn off in :" , _)
    time.sleep(1)
print("Bye!")
sys.exit()