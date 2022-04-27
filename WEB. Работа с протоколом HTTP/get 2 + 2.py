import requests

s = input()
x = input()
r = requests.get(f'{s}:{x}?a={input()}&b={input()}').json()
a = r['result']
a.sort()
print(*a)
print(r['check'])
