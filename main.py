import requests
import aiohttp
import ssl
import certifi
import asyncio


# for i in range(10):
#     response = requests.get('http://192.168.0.110:80')
#     print(response.status_code)

async def my_request():
    ssl_contest = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_contest)
    async with aiohttp.ClientSession(connector=conn) as sess:
        async with sess.get('http://192.168.0.110:80') as response:
            print(response.status)

async def main():
    tasks = [my_request() for _ in range(10)]
    await asyncio.gather(*tasks)

asyncio.run(main())
