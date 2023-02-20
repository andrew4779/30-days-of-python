import numpy as np


numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array:' , numpy_array_from_list)
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array:' , numpy_array_from_list)
ten_times_original = numpy_array_from_list ** 2
print(ten_times_original)

numpy_int_arr = np.array([1, 2, 3, 4, 5])
numpy_float_arr = np.array([1.1, 2.0, 3.2])

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)