#  测试 asyncio + aiohttp 的效果

import time
import aiohttp
import asyncio


NUMBERS = range(12)
URL = 'http://httpbin.org/get?a={}'


async def fetch_async(a):
    async with aiohttp.request('GET', URL.format(a)) as r:
        data = await r.json()
    return data['args']['a']


if __name__ == "__main__":
    start = time.time()
    event_loop = asyncio.get_event_loop()
    tasks = [fetch_async(num) for num in NUMBERS]
    results = event_loop.run_until_complete(asyncio.gather(*tasks))
    for num, result in zip(NUMBERS, results):
        print('fetch({}) = {}'.format(num, result))
    end = time.time()
    print(end - start)
