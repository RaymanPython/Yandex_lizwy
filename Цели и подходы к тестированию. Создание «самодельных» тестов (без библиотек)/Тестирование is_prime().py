from yandex_testing_lesson import is_prime


def testing():
    test_values = (
        (2, True),
        (10, False),
        (23, True),
        (14, False),
        (4, False),
        (100, False)
    )
    for key, value in test_values:
        if is_prime(key) != value:
            return False
    return True


if testing():
    print('YES')
else:
    print('NO')
