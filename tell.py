

ab = open("D:/VS CODE/python/work.txt","r")

# tell function

# print(ab.tell())
# print(ab.read(5))
# print(ab.tell())


# seek function


# print(ab.readlines())
# print(ab.tell())
print(ab.seek(2))
print(ab.read(5))
# print(ab.read())


ab.close()
