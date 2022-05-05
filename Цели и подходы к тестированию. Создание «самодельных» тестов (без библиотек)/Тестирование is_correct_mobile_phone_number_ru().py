from yandex_testing_lesson import is_correct_mobile_phone_number_ru


def testing():
    test_values = (
        ("+7(900)1234567", True),
        ("+7 999 123-45-67", True),
        ("87957777777", True),
        ("879577777777", False),
        ("+7(900)123456", False),
        ("+7 999 123-45--67", True),
        ("+7)900)123456", False),
        ("+6(900)1234567", False),
        ("+7(900)12", False),
        ("8(900)123 4567", True),
        ("8(90)123 4567", False),
        ("", False),
        ("+(79031234567)", False),
        ("+7903(123)4567", False),
    )
    for key, value in test_values:
        if is_correct_mobile_phone_number_ru(key) != value:
            return False
    return True


print("YES") if testing() else print("NO")
