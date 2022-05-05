from yandex_testing_lesson import is_palindrome


def testing():
    test_values = (
        ("a", True),
        ("gggf", False),
        ("ssssss", True),
        ("ada", True),
        ("nbkj", False),
        ("ffggfsf", False),
        ("cxxxxc", True)
    )
    for key, value in test_values:
        if is_palindrome(key) != value:
            return False
    return True


if testing():
    print('YES')
else:
    print("NO")

ы
