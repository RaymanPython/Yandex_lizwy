import sys
import json
import csv
import requests
import sqlite3

s = input()
a = []
for i in sys.stdin:
    if i.strip() == '':
        break
    a.append(i.strip())
b = list(map(lambda x: len(x.split(s)), a))
min_i = len(b) - 1
i = min_i
while i >= 0:
    if b[i] >= b[min_i]:
        min_i = i
    i -= 1
b = a[min_i].split(s)
max_i = 0
for i in range(len(b)):
    if len(b[i]) > len(b[max_i]):
        max_i = i
    elif len(b[i]) == len(b[max_i]):
        if b[i] < b[max_i]:
            max_i = i
print(b[max_i])
