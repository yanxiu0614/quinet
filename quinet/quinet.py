# coding:utf-8


"""
    :copyright: © 2018 by the yanxiu.
    :license: BSD, see LICENSE for more details.
"""

import sys

from quinet.quinetexception import QuinetException

import gevent.pool
from gevent import monkey
monkey.patch_all()

if sys.version > '3':
    from queue import Queue
else:
    from Queue import Queue


class Quinet:
    def __init__(
            self,
            method,
            callback=None,
            timeout=100,
            block_number=3000,
            pool_size=500):

        """
        method非空,但是callback可空,当callback为非空时,method需有返回值,否则异常,后续需加上校验;
        block_number每次放入内存中的量.该设置与内存有关;
        协程池数量,与内存和带宽相关;
        timeout超时时间为运行完成block_number数量数据的超时时间;
        """

        self.waiting_queue = Queue()
        if(method is None):
            raise QuinetException('The method is None')
        self.method = method
        self.callback = callback
        self.block_number = block_number
        self.pool_size = pool_size
        self.timeout = timeout

    def get_block_data(self):
        temp_list = list()
        queue_size = self.waiting_queue.qsize()
        if(queue_size >= self.block_number):
            for n in range(self.block_number):
                temp_list.append(self.waiting_queue.get_nowait())
        else:
            for n in range(queue_size):
                temp_list.append(self.waiting_queue.get_nowait())
        return temp_list

    def run(self):
        while True:
            if (self.waiting_queue.empty()):
                break
            else:
                temp_list = self.get_block_data()
                coroutine_pool = gevent.pool.Pool(self.pool_size)
                for data in temp_list:
                    coroutine_pool.apply_async(
                        self.method, args=(
                            data,), callback=self.callback)
                coroutine_pool.join(timeout=self.timeout)
                coroutine_pool.kill()
