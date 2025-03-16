import numpy as np

# ----------------- NumPy 1D Array Functions -----------------
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# Mathematical Operations
print("Sum:", np.sum(array_1d))
print("Mean:", np.mean(array_1d))
print("Max:", np.max(array_1d))
print("Min:", np.min(array_1d))
print("Standard Deviation:", np.std(array_1d))
print("Variance:", np.var(array_1d))
print("Cumulative Sum:", np.cumsum(array_1d))
print("Cumulative Product:", np.cumprod(array_1d))

# Indexing and Slicing
print("First 3 Elements:", array_1d[:3])
print("Last 2 Elements:", array_1d[-2:])

# Reshape
reshaped_1d = array_1d.reshape(5, 1)
print("Reshaped 1D Array to 5x1:\n", reshaped_1d)

# ----------------- NumPy 2D Array Functions -----------------
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", array_2d)

# Mathematical Operations
print("Sum of Each Row:", np.sum(array_2d, axis=1))
print("Sum of Each Column:", np.sum(array_2d, axis=0))
print("Mean of Each Column:", np.mean(array_2d, axis=0))
print("Max in Each Row:", np.max(array_2d, axis=1))
print("Min in Each Column:", np.min(array_2d, axis=0))

# Transpose
print("Transpose:\n", array_2d.T)

# Flatten Array
print("Flattened Array:", array_2d.flatten())

# Random Functions
random_array = np.random.rand(3, 3)
print("\nRandom Array:\n", random_array)

# Identity Matrix
identity_matrix = np.eye(3)
print("Identity Matrix:\n", identity_matrix)

# Diagonal Elements
print("Diagonal of 2D Array:", np.diag(array_2d))

# Dot Product
dot_product = np.dot(array_2d, array_2d.T)
print("Dot Product of 2D Array with its Transpose:\n", dot_product)

# Creating an Array with a Range
range_array = np.arange(1, 11, 2)  # Start=1, End=10, Step=2
print("Range Array:", range_array)

# Creating an Array of Zeros and Ones
zeros_array = np.zeros((3, 3))
ones_array = np.ones((2, 2))
print("\nZeros Array:\n", zeros_array)
print("Ones Array:\n", ones_array)

# Random Integers
random_ints = np.random.randint(1, 100, (3, 3))
print("\nRandom Integers Array:\n", random_ints)

# Linespace 
random_line=np.linspace(1,5,10)
print('\nRandom Integers Array with a fix sepration:\n',random_line)
