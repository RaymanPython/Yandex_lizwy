import re
import sys


def is_correct_mobile_phone_ru(n):
    n = n.replace(' ', '')
    s = r'^(\+7|8)?(([\(]{1}\d{3}[\)]{1})|([\-]?\d{3}[\-]?)|' \
        r'(\d{3}))?([ \-])?(\d{3}[\- ]*\d{2}[\- ]*\d{2})$'
    r = re.search(s, n)
    return r


for i in sys.stdin:
    if is_correct_mobile_phone_ru(i.rstrip()):
        print('YES')
    else:
        print('NO')
