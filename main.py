def password_has_8_characters(password):
    return len(password) >= 8


def password_has_special_symbol(password):
    for character in password: # !@#$%
        if character in ["!","@","#","$","%"]:
            return True

    return False


def password_has_at_least_2_digits(password):
    digit_counter = 0
    for character in password:
        if character in ["0","1","2","3","4","5","6","7","8","9"]:
            digit_counter += 1
            if digit_counter >= 2:
                return True

    return False



def main():
    password = input("Enter your password: ")

    conditions = [
        password_has_8_characters(password),
        password_has_special_symbol(password),
        password_has_at_least_2_digits(password)
    ]

    if all(conditions):
        print("Password is strong")
    else:
        print("Password is not strong")


if __name__ == '__main__':
    main()