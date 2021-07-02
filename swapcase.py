def swap_case(s):
    word = ""
    for letter in s:
        if letter.isupper():
           a = letter.lower()
           word = word + a
        elif letter.islower():
            a = letter.upper()
            word = word + a
        else:
            word = word + letter
    return word
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
