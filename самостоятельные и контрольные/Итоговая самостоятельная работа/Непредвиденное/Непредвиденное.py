import requests


def unexpected(**data):
    answers = dict()
    a = requests.get(f'http://{data["host"]}:{data["port"]}').json()
    for i in data:
        if i == 'host' or i == 'port':
            continue
        else:
            if a[i] != data[i]:
                answers[i] = data[i]
    return answers
