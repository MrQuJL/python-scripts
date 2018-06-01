import base64

en = base64.b64encode(b'binary\x00string')
print(en)
de = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(de)

base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')

base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')

base64.urlsafe_b64decode('abcd--__')

