import os
import sys

import pygame
import requests

map_request = "https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Австралия&format=json"
s = requests.get(map_request).json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]['pos']
x, y = map(str, s.split())
print(x, y)
map_request = f"http://static-maps.yandex.ru/1.x/?ll={x},{y}&spn=20,15&l=map"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)
ы
