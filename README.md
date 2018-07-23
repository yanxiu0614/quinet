Quinet
=====

Quinet是一个简单的客户端网络并发框架, 其基于Python的gevent库(即协程), 并兼容Python2和Python3。Quinet旨在让任何一个Python开发者只需几行代码即可享受网络高并发带来的效率和乐趣.


安装
----------

git clone https://github.com/yanxiu0614/quinet.git


示例
----------------

```
from quinet import Quinet

def get_num(num):
    time.sleep(10)
    print(num)

client = Quinet(method=get_num)

for num in range(100):
    client.waiting_queue.put(num)

client.run()

# 花费:10.016秒
```


Links
-----

* Website: http://www.gevent.org
