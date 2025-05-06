import numpy as np 
a = np.array ([1,2,3,4,5])
b = np.array ([6,7,8,9,10])
print(a)
print(b)

arr = np.array(["Hello", 42, 3.14])
print(arr)

Array2D = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])
print(Array2D)

array3D = np.array([[[1,2,3], [4,5,6]],
[[7,8,9], [10,11,12]],
[[13,14,15], [16,17,18]]])
print(array3D)

data = np.array([[1,2,3,4], [5,6,7,8,]])
print(data.shape)
print(data[0,3])
print(data[1,2])
print(data[:, 2])
print(data[1, :])
print(data[:, 1:3])
print(data[1, 1:4])
print(data[:, 1:4])
print(data.diagonal(2))
print(data.diagonal(3))

empty=np.zeros((4,4), dtype="int")
empty[1:3, 1] = [9,5]
print(empty)

c = np.array([3,6,9,12])
d = np.array([2,4,6,8])
print(np.add(c,d))
print(np.subtract(c,d))
print(np.multiply(c,d))
print(np.divide(c,d))

print(c.sum(), d.sum())
print(c.min(), d.min())
print(c.max(), d.max())

c = np.array([3,6,9,12])
d = np.array([2,4,6,8])
print(np.add(c,d))
print(np.subtract(c,d))
print(np.multiply(c,d))
print(np.divide(c,d))

print(c.sum(), d.sum())
print(c.min(), d.min())
print(c.max(), d.max())