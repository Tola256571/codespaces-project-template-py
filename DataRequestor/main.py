from time import sleep
#from snap7.server import mainloop
import requests

res = requests.get("https://api.openaq.org/v2/locations/2178" headers={"X-API-Key": "15786ff39999dd095128abc999dafa4bf3661a7f0fe50e4217820d2dac66d8dc"})

#https://docs.openaq.org/docs/getting-started

url = "https://api.openaq.org/v2/locations?limit=100&page=1&offset=0&sort=desc&radius=25000&country=PL&city=Wroc%C5%82aw&order_by=lastUpdated&dump_raw=false"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)




