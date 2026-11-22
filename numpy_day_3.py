'''
CREATING NUMPY ARRAY

A array is a data structure that stores multiple elements in a  organized way
IN numpy array can have one or more dimensions array

'''
import numpy as np
a=np.array([1,2,3,4,5])       #1D array
print("1D ARRAY=",a)
b=np.array([[1,2],[3,4]])     # 2D array
print("2D ARRAY=",b)
C=np.array([
            [[1,2],[3,4]],    #3D array
            [[5,6],[7,8]]
            ])
print("3D ARRAY=",C)
print(type(C))

#Creating array using tuple
arr=np.array(((1,2),(3,4)))
print("tuple-array=",arr)

#creating a array using specifying datatype
brr=np.array([1,2,3,4,5],dtype=float)
print("specifying datatype=",brr)