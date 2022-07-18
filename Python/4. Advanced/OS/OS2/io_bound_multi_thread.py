import concurrent.futures
import threading
import requests
import time

# 쓰레드 로컬 사용
thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def request_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"[Read Contents : {len(response.content)}, Status Code : {response.status_code}] from {url}")


def request_all_site(urls):
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(request_site, urls)


def main():
    urls = ["https://www.jython.org", "http://olympus.realpython.org/dice", "https://realpython.com/"]

    start_time = time.time()
    request_all_site(urls)
    duration = time.time() - start_time
    print(f"Downloaded {len(urls)} sites in {duration} seconds")


if __name__ == "__main__":
    main()