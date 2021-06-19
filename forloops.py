friends = ["Jim", "Karen", "Kevin"]
for name in friends:
    print(name)

brand = "Giraffe Academy"
for bname in brand:
    print(bname)

print("\n")
for index in range(3,10): #10 will not be included
    print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print( str(index) +" iteration")