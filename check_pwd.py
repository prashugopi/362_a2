def check_pwd(password):
    lower = 0

    if len(password) < 8 or len(password) > 20:
        return False
    
    for i in password:
        if i.islower():
            lower += 1
    if lower == 0:
        return False

    return True