import requests
import json

cleverbot_key="CC1mfFU0_3B1fo5cRiSmjg0fJ1g"


clever_url = "http://www.cleverbot.com/getreply"

def gen_url(zip_code):
    
    return clever_url + ",us" + "&APPID=" + cleverbot_key
print (gen_url('08003'))
#r = requests.get(gen_url("11417"))
# = r.json()

#print(data)