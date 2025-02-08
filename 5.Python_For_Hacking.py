# To make requset for any site
import requests
url = "http://testphp.vulnweb.com"
response = requests.get(url, verify=False)
print(response.text)
print(response.status_code)