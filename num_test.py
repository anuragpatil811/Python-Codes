import numpy as np

# Create a NumPy array
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])

# Perform element-wise addition
sum_array = array1 + array2

# Calculate the mean of the resulting array
mean_value = np.mean(sum_array)

print("Array 1:", array1)
print("Array 2:", array2)
print("Sum of Arrays:", sum_array)
print("Mean of Sum Array:", mean_value)
