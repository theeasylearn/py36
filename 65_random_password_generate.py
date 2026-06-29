import random
import string

def GeneratePassword(length = 10):
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    size = len(letters) - 1
    count = 0
    password = []

    while count < length:
        password.append(letters[random.randint(0, size)])
        count = count + 1
        
    return "".join(password)


print(GeneratePassword())