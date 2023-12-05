import requests
import re

url = 'https://www.agiratech.com/install-requests-library-in-python'
response = requests.get(url)
html = response.text


pattern = r'href="([^"]+\.\w+)"'


matches = re.findall(pattern, html)

#
print("Имена файлов, указанные в ссылках на другие документы:")
for match in matches:
    print(match)
