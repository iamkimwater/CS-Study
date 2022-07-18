from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.request
import logging

URLS = ['http://www.daum.net/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']


def load_data(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


def main():
    logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("나는 메인 쓰레드. 작업을 시작한다!")
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(load_data, url, 60): url for url in URLS}
        for future in as_completed(future_to_url):
            try:
                data = future.result()
                url = future_to_url[future]
                print('%r page is %d bytes' % (url, len(data)))
            except Exception as e:
                print('%r generated an exception: %s' % (url, e))
    logging.info("나는 메인 쓰레드. 작업을 종료한다!")


if __name__ == '__main__':
    main()