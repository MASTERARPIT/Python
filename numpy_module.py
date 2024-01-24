import numpy as np 

array_one = np.array([1,2,3,4,5])
array_two = np.array([6,7,8,9,10])

print(array_one)
print(array_two)

array_one += 5
print(array_one)

array_two *= 10

print (array_two)

sum1=np.sum(array_one)
print (sum1)
sum2=np.sum(array_one+array_two)
print (sum2)
largest_element = np.max(array_one)
smallest_element = np.min(array_two)
print (largest_element)
print (smallest_element)