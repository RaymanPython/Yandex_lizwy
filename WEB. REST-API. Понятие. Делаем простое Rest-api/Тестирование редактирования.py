from requests import put

print(put('http://localhost:5000/api/jobs').json())

print(put('http://localhost:5000/api/jobs',
          json={'id': 'Заголовок'}).json())

print(put('http://localhost:5000/api/jobs',
          json={'id': '5',
                'name': 'ДЗ'}).json())
print(put('http://localhost:5000/api/jobs',
          json={'id': '-1',
                'name': 'ДЗ'}).json())

print(put('http://localhost:5000/api/jobs').json())
