#1D array bcuz 1 row or direction me hai ya length
import numpy as np
#a = np.array([2,3,2,2,3,2])
#print(a)

#2D array of 2*6

#a = np.array([[2,3,2,2,3,2],[2,3,2,2,3,2]])
#print(a)

#2D array of 4*3
#a = np.array([[2,3,2],[2,3,2],[3,4,5],[3,4,6]])
#print(a)

#2D array of 5*5

#a = np.array([[2,3,2,4,5],[2,3,2,3,7],[3,4,5,6,9,],[3,4,6,3,5],[2,3,5,2,4]])
#a = np.array([[2,3,2,3,7],[3,4,5,6,9,],[3,4,6,3,5],[2,3,5,2,4]])
a = np.array([2,3,2,3,7])
print(a.itemsize)
print(a.dtype)
#print(a.shape)
#print(a.size)
print("The maximum element", a.max())
#a1=a.reshape(5,4)
#print(a1)
#print(a1.shape)