from quinet.quinet import Quinet
import requests

url_list = ['http://qq.com/', 'http://baidu.com', 'http://taobao.com']


def get_status_code(url):
    try:
        res = requests.get(url)
    except Exception as e:
        pass
        res = 0
    return res.status_code


def print_status_code(code):
    print(code)


client = Quinet(method=get_status_code, callback=print_status_code)

for url in url_list:
    client.waiting_queue.put(url)

client.run()


"""

def get_status_code(url):
    try:
        res=requests.get(url)
    except Exception as e:
        pass
        res=0
    print(res.status_code)

client=Quient(method=get_status_code)

for url in url_list:
    client.waiting_queue.put(url)

client.run()

"""
