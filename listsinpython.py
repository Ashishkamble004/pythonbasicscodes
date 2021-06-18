friends = ["Kevin", "Karen", "Jim","dwight", "pam", "Jim"]
lucky_numbers = [4, 5, 6, 7, 8, 9]
print(friends[2])
#friends.extend(lucky_numbers)
#lucky_numbers.extend(friends)
print(friends)
print(lucky_numbers)
friends.insert(3,"Creed")
print(friends)
friends.remove("Creed")
print(friends)
friends.clear
print(friends)
friends.pop()
print(friends)
print(friends.count("Jim"))
friends.sort()
lucky_numbers.sort()
print(friends)
print(lucky_numbers)

friends2 = friends.copy()
print (friends2)