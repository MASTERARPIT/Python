
# writing new content to the file
# fp = open("D:/VS CODE/class python/write_demo.txt", 'r+')
# text = "This is a python content"
# fp.write(text)
# fp = open("D:/VS CODE/class python/write_demo.txt", 'r+')

# # fp.seek()
# # print('Done Writing arpit')
# print(fp.read())
# fp.close()

print(end="Enter the Name of File: ")
# fileName = str(input())

try:
  fileHandle = open("D:/VS CODE/class python/write_demo.txt", "r")
  tot = 0

  for char in fileHandle.read():
    if char==' ':
      tot = tot+1
  fileHandle.close()

  if tot>1:
    print("\nThere are " ,tot , " Blank spaces available in the File")
  elif tot==1:
    print("\nThere is only 1 Blank space available in the File")
  else:
    print("\nThere is no any Blank space available in the File!")
except IOError:
  print("\nError Occurred!")

