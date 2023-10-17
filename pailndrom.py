def is_palindrom(in_string):
    forward = " "
    reverse = " "
    #
    for char in in_string:
        print(char,end=" ")
        forward += char
        reverse = char + reverse
    #
    print()
    if forward.lower().strip() == reverse.lower().strip():
    #    print("matched")
        return True
    else:
        return False


print(is_palindrom("ABCDcba"))

print(is_palindrom("MALAYALAM"))

print(is_palindrom("1234321a"))
