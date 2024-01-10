def mul_list(list) :
     
    # Multiply elements one by one
    product = 1
    for i in list:
         product = product * i
    return product
     

list1 = [11, 12, 4, 3]
print(list1)

print("product:",mul_list(list1))