from os import read


employee_file = open("emp.txt", "r")
#firstblock is file path, and second is option would be read-r, write-w, a - append, + read & write)

'''
print(employee_file.readable())
#returns bool if the file is readable or not, it depends on the open mode for the file.
#it will return false if the open mode is 'w', and true if the mode is 'r'
'''
#print(employee_file.read()) #read whole file

'''
print(employee_file.readline()) #read line by line
print(employee_file.readline())
print(employee_file.readline())
'''

print(employee_file.readlines()[1])

'''
for employee in employee_file.readlines():
    print (employee)
'''
employee_file.close()
#close the file at some point after opening it



