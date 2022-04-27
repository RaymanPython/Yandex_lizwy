import requests

response = requests.get(
    "https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Москва,Красная площадь,1&format=json")
json_response = response.json()
print(json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
          "GeocoderMetaData"]["Address"]["formatted"],
      json_response["response"]["GeoObjectCollection"]["featureMember"][0][
