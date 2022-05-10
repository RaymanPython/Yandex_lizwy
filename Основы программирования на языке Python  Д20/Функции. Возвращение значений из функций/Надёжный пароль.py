def password_level(password):
    C = "0123456789"
    f1 = f2 = f3 = False
    if len(password) < 6:
        s = "Недопустимый пароль"
        return s
    elif password.isdigit():
        s = "Ненадежный пароль"
        return s
    for i in password:
        if i.isupper():
            f1 = True
        elif i.islower():
            f2 = True
        elif i in C:
            f3 = True
    if f1 * f2 * f3:
        s = "Надежный пароль"
    elif f1 ^ f2 and not f3:
        s = "Ненадежный пароль"
    else:
        s = "Слабый пароль"
    return s
