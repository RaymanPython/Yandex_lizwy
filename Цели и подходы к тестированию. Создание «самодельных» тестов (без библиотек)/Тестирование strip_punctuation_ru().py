from yandex_testing_lesson import strip_punctuation_ru


def testing():
    test_values = (
        ("Россия. Пять", "Россия Пять"),
        ("Бабушка - хорошая", "Бабушка хорошая"),
        ("Память,  о", "Память о"),
        ("С, С.", "С С"),
        ("", ""),
        ("", ""),
        ("", ""),
        ("", ""),
        ("", ""),
        ("", ""),
    )
    for key, value in test_values:
        if strip_punctuation_ru(key) != value:
            return False
    return True


print("YES") if testing() else print("NO")
