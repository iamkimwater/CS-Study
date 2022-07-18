import asyncio
import aiohttp
import time


async def request_site(session, url):
    async with session.get(url) as response:
        print("Read Contents {0}, from {1}".format(response.content_length, url))


async def request_all_site(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.create_task(request_site(session, url)))
        await asyncio.gather(*tasks)


def main():
    urls = ["https://www.jython.org", "http://olympus.realpython.org/dice", "https://realpython.com/"]

    start_time = time.time()
    loop = asyncio.get_event_loop()
    co = request_all_site(urls)
    loop.run_until_complete(co)
    end_time = time.time()
    duration = end_time - start_time
    print(f"Downloaded {len(urls)} sites in {duration} seconds")


if __name__ == "__main__":
    main()