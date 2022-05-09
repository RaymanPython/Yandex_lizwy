from requests import post

print(post('http://localhost:5000/api/jobs').json())

print(post('http://localhost:5000/api/jobs',
           json={'id': 'Заголовок'}).json())

print(post('http://localhost:5000/api/jobs',
           json={'id': '5',
                 'name': 'ДЗ'}).json())
