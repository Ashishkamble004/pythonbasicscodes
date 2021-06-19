from os import read


employee_file = open("emp.txt", "r")
#firstblock is file path, and second is option would be read-r, write-w, a - append, + read & write)

#print(employee_file.readable())
#returns bool if the file is readable or not, it depends on the open mode for the file.
#it will return false if the open mode is 'w', and true if the mode is 'r'

print(" \n This will read all of the file")
print(employee_file.read())

print (" \n This will print a line from the file")

print(employee_file.readline())
print(employee_file.readline())
employee_file.close()
#close the file at some point after opening it

