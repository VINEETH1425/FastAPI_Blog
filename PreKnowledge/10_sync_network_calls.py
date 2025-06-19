import time
import requests # these requests will be done in the synchronous manner.

def main():
    requests_count=10
    url = "https://httpbin.org/get"
    session = requests.Session()
    for i in range (requests_count):
        print(f"making request : {i}")
        resp = session.get(url)
        if resp.status_code==200:
            pass
    

start = time.time()
main()
end = time.time()
# print("Time elapsed : ",end-start)
print(f"Time elapsed : {end-start}")

# due to this some parts will be so much time, due to this cpu will be remaining idle
# so reduce this we will be doing in the async way.

# (env) D:\FASTAPI\PreKnowledge>python 10_sync_network_calls.py
# making request : 0
# making request : 1
# making request : 2
# making request : 3
# making request : 4
# making request : 5
# making request : 6
# making request : 7
# making request : 8
# making request : 9
# Time elapsed : 51.26500415802002