import numpy as np
import matplotlib.pyplot as plt

myArray = np.array(range(10),dtype=int)
plt.plot(myArray)
plt.show()
print(np.__version__)
print(myArray)