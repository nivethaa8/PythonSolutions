
import math
import time
start_time = time.time()
for y in range (1000000):
    x = math.cos(0.2)
print("%.4f" % x)
print("My program took %.4f seconds to run " % (time.time() - start_time))
