a = 'щи,борщ,щавелевый суп,овсяный суп,суп по-чабански'.split(',')
for i in range(int(input())):
    print(a[i % len(a)])
