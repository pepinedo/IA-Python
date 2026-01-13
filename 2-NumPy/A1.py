import numpy as np

x = np.array([3, 6, 9, 12, 15])

print(type(x))
print(x.dtype)
print(x.ndim)

print("---")
print(x.reshape(1, len(x)))
print(x.reshape(1, len(x)).shape)
print("---")
print(x.reshape(len(x), 1))
print(x.reshape(len(x), 1).shape)