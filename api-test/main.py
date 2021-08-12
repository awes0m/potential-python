import requests

api_key =""
owm_endpoint =""

w_params={
    "Lat":23.5,
    "Long":12,
    "appid":api_key
}
response= requests.get(owm_endpoint,params=w_params)
print(response.status_code)
print(response.json())