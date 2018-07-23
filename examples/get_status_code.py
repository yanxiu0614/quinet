from quinet.quinet import Quinet
import requests

url_list = ['http://qq.com/', 'http://baidu.com', 'http://taobao.com']

def get_status_code(url):
    try:
        res=requests.get(url)
        status_code=res.status_code
    except Exception as e:
        status_code=0
    return(status_code)

def print_status_code(status_code):
    print(status_code)

client = Quinet(method=get_status_code, callback=print_status_code)

for url in url_list:
    client.waiting_queue.put(url)

client.run()


"""
from quinet.quinet import Quinet
import requests

url_list = ['http://qq.com/', 'http://baidu.com', 'http://taobao.com']

def get_status_code(url):
    try:
        res=requests.get(url)
        status_code=res.status_code
    except Exception as e:
        status_code=0
    print(status_code)

client=Quinet(method=get_status_code)

for url in url_list:
    client.waiting_queue.put(url)

client.run()

"""
