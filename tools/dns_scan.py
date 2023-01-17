import requests, json, http.client
from tqdm.auto import tqdm
from time import sleep
from sched import sched
API_URL = "https://crt.sh/?q={}&output=json"
subdomains = set()

domain = str(input("Masukkan subdomain: "))



class loading:

    condition = True

    def loop_loading(condition):
        n_dots = 0
        text='loading'
        delay=0.5
        print(end=text)

        while condition:
            if n_dots == 3:
                print(end='\b\b\b', flush=True)
                print(end='   ',    flush=True)
                print(end='\b\b\b', flush=True)
                n_dots = 0
            else:
                print(end='.', flush=True)
                n_dots += 1
            sleep(delay)
    def stop():
        return False

def crtsh(domain):
    try:
        response = requests.get(API_URL.format(domain), timeout=25)
        if response.ok:
            content = response.content.decode('UTF-8')
            jsondata = json.loads(content)
            for i in range(len(jsondata)):
                name_value = jsondata[i]['name_value']
                if name_value.find('\n'):
                    subname_value = name_value.split('\n')
                    for subname_value in subname_value:
                        if subname_value.find('*'):
                            if subname_value not in subdomains:
                                subdomains.add(subname_value)
        else: 
            print('request timeout')
    except:
        pass

isloading = True
r = loading()
r.condition = False
print(r.condition)
# crtsh(domain)
# print(type(subdomains))
# print(list(subdomains))
# print("berhasil")

# output
# number = 1
# if domain:
#     for subdomain in subdomains:
#         try:
#             connection = http.client.HTTPSConnection(f"{subdomain}")
#             connection.request("GET", "/") 
#             response = connection.getresponse()
#             print(f"{number}. {subdomain} - {response.status} {response.reason}")
#         except KeyboardInterrupt:
#             print("-"*30)
#             print("Kode diberhentikan")
#             quit()
#         except:
#             print(f"{number}. {subdomain} - ERROR")
#             pass
#         connection.close()
#         number += 1