import requests

response = requests.get(
    "https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=%D0%9F%D0%B5%D1%82%D1%80%D0%BE%D0%B2%D0%BA%D0%B0,%2038&format=json")
json_response = response.json()
print(json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
          "GeocoderMetaData"]["Address"]["postal_code"])
