import requests
import time


def request_all_site(urls):
    with requests.Session() as session:
        for url in urls:
            with session.get(url) as response:
                print(f"[Read Contents : {len(response.content)}, Status Code : {response.status_code}] from {url}")


def main():
    urls = ["https://www.jython.org", "http://olympus.realpython.org/dice", "https://realpython.com/"]

    start_time = time.time()
    request_all_site(urls)
    end_time = time.time()
    duration = end_time - start_time
    print(f"{duration}")


if __name__ == "__main__":
    main()