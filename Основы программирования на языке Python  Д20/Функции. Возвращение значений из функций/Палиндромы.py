def palindrome(s):
    s = ''.join(s.split())
    s = s.lower()
    if s == s[::-1]:
        return 'Палиндром'
    else:
        return 'Не палиндром'
