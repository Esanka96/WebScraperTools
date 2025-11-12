import urllib.parse
import json

encoded_string = "%7B%22name%22%3A%22vi-VN%22%2C%22language%22%3A1%2C%22prefix%22%3A%22vi%22%7D"
decoded_string = urllib.parse.unquote(encoded_string)

json_data = json.loads(decoded_string)

# Iterate through the dictionary to get keys and values
for key, value in json_data.items():
    print(f"{key} : {value}")