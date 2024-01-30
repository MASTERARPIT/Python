# import numpy as np 

# array_one = np.array([1,2,3,4,5])
# array_two = np.array([6,7,8,9,10])

# print(array_one)
# print(array_two)

# array_one += 5
# print(array_one)

# array_two *= 10

# print (array_two)

# sum1=np.sum(array_one)
# print (sum1)
# sum2=np.sum(array_one+array_two)
# print (sum2)
# largest_element = np.max(array_one)
# smallest_element = np.min(array_two)
# print (largest_element)
# print (smallest_element)

#----------------------------------------------------------------------------------

# from scipy.special import cbrt
# cube_root = cbrt([81,64])
# print("cube root is ",cube_root)

import pandas as pd 
data = [1,2,3,4,5,6,7]
data_series = pd.Series(data) 
print(data_series)
print(type(data_series))

dict = {
    'Roll No':[10,12,15,18],
    'Name':["Rohan","Anush","Ashish","Vivek"],
    'Branch':["ECE","IT","CSE","IT"]
}
df = pd.DataFrame(dict)
print(df)