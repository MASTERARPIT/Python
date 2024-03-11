ab = open("D:/VS CODE/python/work.txt","r+")

# tot=0
# vow="aeiouAEIOU"

# for i in ab.read():
#     if i in vow:
#         tot=tot+1
# ab.close()
# print(tot)
b=[]
a="india"

for i in ab.read():
    for j in i.split():
        if j == a :
            print(ab.write(i.capitalize()))

ab.close()
