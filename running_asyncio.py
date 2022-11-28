"""
@author:    Krzysztof Brzozowski
@file:      test_asyncio
@time:      28/11/2022
@desc:      
"""
import time

import httpx as httpx
import asyncio

# async def hello():
#     print('hello')
#
#
# async def main():
#     await hello()
#     await hello()
#     await hello()
#
urls = '''https://via.placeholder.com/600/92c952
https://via.placeholder.com/600/771796
https://via.placeholder.com/600/24f355
https://via.placeholder.com/600/d32776
https://via.placeholder.com/600/f66b97
https://via.placeholder.com/600/56a8c2
https://via.placeholder.com/600/b0f7cc
https://via.placeholder.com/600/54176f
https://via.placeholder.com/600/51aa97
https://via.placeholder.com/600/810b14
https://via.placeholder.com/600/92c952
https://via.placeholder.com/600/771796
https://via.placeholder.com/600/24f355
https://via.placeholder.com/600/d32776
https://via.placeholder.com/600/f66b97
https://via.placeholder.com/600/56a8c2
https://via.placeholder.com/600/b0f7cc
https://via.placeholder.com/600/54176f
https://via.placeholder.com/600/51aa97
https://via.placeholder.com/600/810b14
https://via.placeholder.com/600/92c952
https://via.placeholder.com/600/771796
https://via.placeholder.com/600/24f355
https://via.placeholder.com/600/d32776
https://via.placeholder.com/600/f66b97
https://via.placeholder.com/600/56a8c2
https://via.placeholder.com/600/b0f7cc
https://via.placeholder.com/600/54176f
https://via.placeholder.com/600/51aa97
https://via.placeholder.com/600/810b14
https://via.placeholder.com/600/92c952
https://via.placeholder.com/600/771796
https://via.placeholder.com/600/24f355
https://via.placeholder.com/600/d32776
https://via.placeholder.com/600/f66b97
https://via.placeholder.com/600/56a8c2
https://via.placeholder.com/600/b0f7cc
https://via.placeholder.com/600/54176f
https://via.placeholder.com/600/51aa97
https://via.placeholder.com/600/810b14
https://via.placeholder.com/600/92c952
https://via.placeholder.com/600/771796
https://via.placeholder.com/600/24f355
https://via.placeholder.com/600/d32776
https://via.placeholder.com/600/f66b97
https://via.placeholder.com/600/56a8c2
https://via.placeholder.com/600/b0f7cc
https://via.placeholder.com/600/54176f
https://via.placeholder.com/600/51aa97
https://via.placeholder.com/600/810b14
https://via.placeholder.com/600/92c952
https://via.placeholder.com/600/771796
https://via.placeholder.com/600/24f355
https://via.placeholder.com/600/d32776
https://via.placeholder.com/600/f66b97
https://via.placeholder.com/600/56a8c2
https://via.placeholder.com/600/b0f7cc
https://via.placeholder.com/600/54176f
https://via.placeholder.com/600/51aa97
https://via.placeholder.com/600/810b14
https://via.placeholder.com/600/92c952
https://via.placeholder.com/600/771796
https://via.placeholder.com/600/24f355
https://via.placeholder.com/600/d32776
https://via.placeholder.com/600/f66b97
https://via.placeholder.com/600/56a8c2
https://via.placeholder.com/600/b0f7cc
https://via.placeholder.com/600/54176f
https://via.placeholder.com/600/51aa97
https://via.placeholder.com/600/810b14
https://via.placeholder.com/600/92c952
https://via.placeholder.com/600/771796
https://via.placeholder.com/600/24f355
https://via.placeholder.com/600/d32776
https://via.placeholder.com/600/f66b97
https://via.placeholder.com/600/56a8c2
https://via.placeholder.com/600/b0f7cc
https://via.placeholder.com/600/54176f
https://via.placeholder.com/600/51aa97
https://via.placeholder.com/600/810b14
https://via.placeholder.com/600/92c952
https://via.placeholder.com/600/771796
https://via.placeholder.com/600/24f355
https://via.placeholder.com/600/d32776
https://via.placeholder.com/600/f66b97
https://via.placeholder.com/600/56a8c2
https://via.placeholder.com/600/b0f7cc
https://via.placeholder.com/600/54176f
https://via.placeholder.com/600/51aa97
https://via.placeholder.com/600/810b14
https://via.placeholder.com/600/92c952
https://via.placeholder.com/600/771796
https://via.placeholder.com/600/24f355
https://via.placeholder.com/600/d32776
https://via.placeholder.com/600/f66b97
https://via.placeholder.com/600/56a8c2
https://via.placeholder.com/600/b0f7cc'''

import os
import threading

# def print_process_id():
# ...   print(threading.current_thread(), os.getpid())

async def a(url):
    # print('a: started')
    # await asyncio.sleep(0.2)
    # print('a: finished')
    # return 'a'
    async with httpx.AsyncClient(base_url=url) as client:
        print(threading.current_thread(), os.getpid())
        return await client.request(method='GET', url=url, data=None)

async def b():
    # print('b: started')
    # await asyncio.sleep(0.1)
    # print('b: finished')
    # return 'b'
    async with httpx.AsyncClient(base_url='https://via.placeholder.com/600/fdf73e.jpg') as client:
        print(threading.current_thread(), os.getpid())
        return await client.request(method='GET', url='https://via.placeholder.com/600/fdf73e.jpg', data=None)

async def c():
    # print('c: started')
    # await asyncio.sleep(0.3)
    # print('c: finished')
    # return 'c'
    async with httpx.AsyncClient(base_url='https://via.placeholder.com/600/fdf73e.jpg') as client:
        print(threading.current_thread(), os.getpid())
        return await client.request(method='GET', url='https://via.placeholder.com/600/fdf73e.jpg', data=None)


async def main():
    start = time.time()
    todo = [a(f'{line.strip()}.jpg') for line in urls.split('\n')]
    # todo = [a() for _ in range(100)]
    for coro in asyncio.as_completed(todo):
        result = await coro
        print(result)
    print(f'end time {time.time() - start}')


async def request_async(some_arg):
        async with httpx.AsyncClient(base_url='https://via.placeholder.com/600/fdf73e.jpg') as client:
            print(threading.current_thread(), os.getpid())
            return await client.request(method='GET', url='https://via.placeholder.com/600/fdf73e.jpg', data=None)


async def runner():
    for n in range(30):
        await request_async(n)


if __name__ == '__main__':
    asyncio.run(main())

