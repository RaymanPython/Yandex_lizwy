import os
import sys

import pygame
import requests


class RESP:

    def __init__(self):
        self.loc = 0
        self.name = "map.png"
        self.xp = 0.1
        self.yp = 0.01
        self.delta_xp = 0.01
        self.delta_yp = 0.01

    def get(self, delta_loc):
        self.loc += delta_loc
        self.xp += delta_loc * self.delta_xp
        self.yp += delta_loc * self.delta_yp
        a = ['Спартак Москва', 'Динамо Москва', 'Стадион Лужники Москва']
        map_request = f"https://static-maps.yandex.ru/1.x/?l=map&spn=0.2,0.2&pt="
        for i in range(len(a)):
            map_request1 = f"https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={a[i]}&format=json"
            s = requests.get(map_request1).json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"][
                "Point"]['pos']
            x, y = map(str, s.split())
            if i == len(a) - 1:
                map_request += f'{x},{y},{1 + i}'
            else:
                map_request += f'{x},{y},{1 + i}~'
        map_request += ',ya-ru'
        print(map_request)
        self.response = requests.get(map_request)

    def save(self):
        with open(self.name, "wb") as file:
            file.write(self.response.content)


map_resp = RESP()
map_resp.get(0)
map_resp.save()

pygame.init()
screen = pygame.display.set_mode((450, 450))

while pygame.event.wait().type != pygame.QUIT:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(pygame.image.load(map_resp.name), (0, 0))
    pygame.display.flip()
pygame.quit()
ф
