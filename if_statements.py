is_male = True
is_tall = False

if is_male and is_tall:
    print("You are tall male")
elif is_male and not(is_tall):
    print("you are short male ")
elif not(is_male) and not(is_tall):
    print("you are not a male and not tall")
else:
    print ("You are neither male nor tall or both")