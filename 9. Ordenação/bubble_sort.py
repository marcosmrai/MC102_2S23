import numpy as np
import matplotlib.pyplot as plt
import time

def lindinha_sort(v):
    for i in range(0, len(v)):
            for j in range(1, len(v)-i):
                if v[j-1]>v[j]:
                    (v[j-1], v[j]) = (v[j], v[j-1])
    return v

tempos = []
for n in np.arange(5000, step=50):

    
    v = list(np.random.randint(1000, size=n))

    start = time.perf_counter()

    v = lindinha_sort(v)

    tempos.append(time.perf_counter()-start)

plt.scatter(np.arange(5000, step=50), tempos)
plt.show()