import numpy as np


arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)


print("First Element:", arr[0])
print("Last Element:", arr[-1])

print("Elements from index 1 to 3:", arr[1:4])

print("Addition:", arr + 10)
print("Multiplication:", arr * 2)
print("Square:", arr ** 2)

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

print("NumPy fundamentals completed")
