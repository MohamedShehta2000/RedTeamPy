import requests
url = "http://testphp.vulnweb.com"
payload = {"username":"admin","password":"admin"}
response = requests.post(url, data=payload, verify=False)
print(response.content)
print(response.status_code)
