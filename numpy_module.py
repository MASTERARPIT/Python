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

# import pandas as pd 
# data = [1,2,3,4,5,6,7]
# data_series = pd.Series(data) 
# print(data_series)
# print(type(data_series))

# dict = {
#     'Roll No':[10,12,15,18],
#     'Name':["Rohan","Anush","Ashish","Vivek"],
#     'Branch':["ECE","IT","CSE","IT"]
# }
# df = pd.DataFrame(dict)
# print(df)

from tkinter import *

# top = Tk()
# top.mainloop()


#parent = Tk()

#Pack

# redbutton = Button(parent,text="Red",fg="red")
# redbutton.pack(side=LEFT)
# blackbutton = Button(parent, text="Black",fg="Black")
# blackbutton.pack(side=RIGHT)


#Grid

# name = Label(parent,text="Name").grid(row=0,column=0)
# e1=Entry(parent).grid(row=0,column=1)
# Password = Label(parent,text="Password").grid(row=1,column=0)
# e2=Entry(parent).grid(row=1,column=1)
# submit=Button(parent,text="Submit").grid(row=4,column=0)



top = Tk()
top.geometry("400x250")
name=Label(top,text="Name").place(x=30,y=50)
email=Label(top,text="Email").place(x=30,y=90)
Password=Label(top,text="password").place(x=30,y=130)
e1=Entry(top).place(x=80,y=50)
e2=Entry(top).place(x=80,y=90)
e3=Entry(top).place(x=95,y=130)
# submit=Button(top,text="Submit").grid(row=4,column=0)

top.mainloop()
