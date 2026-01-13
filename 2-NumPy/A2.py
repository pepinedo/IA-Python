import numpy as np

values = [10, 20.5, 30]

a_arr = np.array(values, dtype=np.int64)
print(a_arr)
print(a_arr.dtype)
print(a_arr.sum().reshape(-1,1))
print(a_arr.mean(axis=0).reshape(-1,1))

print("-----")

b_arr = np.array(values, dtype=np.float64)
print(b_arr)
print(b_arr.dtype)
print(b_arr.sum().reshape(-1,1))
print(b_arr.mean(axis=0).reshape(-1,1))

# Las medias son diferentes porque los tipos de datos son diferentes