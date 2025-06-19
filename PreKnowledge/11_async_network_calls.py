import time
import asyncio
import aiohttp

async def make_request(session,req_n):
    url = "https://httpbin.org/get"
    print(f"making request : {req_n}")
    async with session.get(url) as resp:
        if resp.status==200:
            await resp.text()


async def main():
    request_count=10
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *[make_request(session,i) for i in range(request_count)]
        )


loop = asyncio.get_event_loop()
start = time.time()
loop.run_until_complete(main())
end = time.time()
print(f"Time elapsed : {end-start}")

# if we observe the time has reduced due to this technique

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
# Time elapsed : 12.986351490020752