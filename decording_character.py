import urllib.parse
import re

encoded_string = "%7B%22name%22%3A%22vi-VN%22%2C%22language%22%3A1%2C%22prefix%22%3A%22vi%22%7D"

encoded_substrings = re.findall(r"%[0-9A-Fa-f]{2}", encoded_string)

decoded_mapping = {}
for encoded in encoded_substrings:
    decoded = urllib.parse.unquote(encoded)
    decoded_mapping[encoded] = decoded
    print(f"Encoded: {encoded} -> Decoded: {decoded}")

print("\nSummary of Decoded Characters:")
for encoded, decoded in decoded_mapping.items():
    print(f"{encoded}: {decoded}")
