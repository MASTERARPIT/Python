

ab = open("D:/VS CODE/python/work.txt","r")

# tell function

# print(ab.tell())
# print(ab.read(5))
# print(ab.tell())


# seek function

print(ab.readline())
print(ab.tell())
ab.seek(6)
print(ab.read(5))
ab.close

ab.close()
