from requests import delete

print(delete('http://localhost:5000/api/job/999').json())
print(delete('http://localhost:5000/api/job/1').json())
print(delete('http://localhost:5000/api/job/a').json())
print(delete('http://localhost:5000/api/job/-1').json())
