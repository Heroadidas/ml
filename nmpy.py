import numpy as np
import time
import random
data = [random.random() for _ in range(1000000)]

numpy_data = np.array(data)
start_time = time.time()
sorted_data = sorted(data)
python_time = time.time() - start_time
print(f"Python sorted: {python_time} seconds")

start_time = time.time()
sorted_numpy_data = np.sort(numpy_data)
numpy_time = time.time() - start_time
print(f"NumPy sort: {numpy_time} seconds")