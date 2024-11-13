import requests

url = "https://i0.wp.com/cinesubz.co/wp-content/uploads/2024/11/eCB06m1KUGilEOlIzb40nkQhVY0.jpg?resize=185%2C278&ssl=1"

response = requests.get(url)

with open("downloaded_image.jpg", "wb") as file:
    file.write(response.content)

