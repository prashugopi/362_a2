def check_pwd(password):

    if len(password) < 8 or len(password) > 20:
        return False
    
    lower = 0
    for i in password:
        if i.islower():
            lower += 1
    if lower == 0:
        return False

    upper = 0
    for i in password:
        if i.isupper():
            upper += 1
    if upper == 0:
        return False

    digits = 0 
    for i in password:
        if i.isdigit():
            digits += 1
    if digits == 0:
        return False

    return True