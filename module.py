
# def add(a,b):
#     result=a+b
#     return result

# def sub(a,b):
#     result=a-b
#     return result

import numpy

array_one = numpy.array([10,11,12])
array_two = numpy.array([[1,2,3],[4,5,6]])

print(array_one)
print(array_two)
print(type(array_two))
print(array_two.ndim) #dimension
print(array_two.size)
print(array_two.dtype)
print(array_two.nbytes)