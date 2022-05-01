import time

from numpy import number

start = time.time()
for i in range(1, 6):
    print(i)
end = time.time()
print(end - start)
