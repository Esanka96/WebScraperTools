import urllib.parse

#encoded_string = "%7B%22v%22%3A%22KKmZxVKZ2E2U6bU2h5t-2Q%22%2C%22Keys%22%3A%22%22%2C%22NciNo_Text%22%3A%22%22%2C%22IsNCI%22%3Afalse%2C%22CAS_Text%22%3A%22%22%2C%22CAS_Type%22%3A%22StartWith%22%2C%22HS_Text%22%3A%22%22%2C%22HS_Type%22%3A%22StartWith%22%2C%22UnNo_Text%22%3A%22%22%2C%22Name_Text%22%3A%22%22%2C%22Name_Type%22%3A%22StartWith%22%2C%22IsVN%22%3Atrue%2C%22IsEN%22%3Afalse%2C%22IdsQD%22%3A%5B%5D%2C%22CongUocIds%22%3A%5B%5D%2C%22NhomQuanLyIds%22%3A%5B%5D%7D"
encoded_string="%7B%22v%22%3A%22uFDyIaYW602aENKvF8agvQ%22%2C%22Keys%22%3A%22%22%2C%22NciNo_Text%22%3A%22%22%2C%22IsNCI%22%3Afalse%2C%22CAS_Text%22%3A%22%22%2C%22CAS_Type%22%3A%22StartWith%22%2C%22HS_Text%22%3A%22%22%2C%22HS_Type%22%3A%22StartWith%22%2C%22UnNo_Text%22%3A%22%22%2C%22Name_Text%22%3A%22%22%2C%22Name_Type%22%3A%22StartWith%22%2C%22IsVN%22%3Atrue%2C%22IsEN%22%3Afalse%2C%22IdsQD%22%3A%5B%5D%2C%22CongUocIds%22%3A%5B%5D%2C%22NhomQuanLyIds%22%3A%5B%5D%7D"

decoded_string = urllib.parse.unquote(encoded_string)
print(decoded_string)
