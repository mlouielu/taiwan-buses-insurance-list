import asyncio
import json
import ssl

import aiohttp
from lxml import etree
from tqdm import tqdm


TQDM_BAR = None


def read_list(filename='bus.csv'):
    with open(filename) as f:
        return [i.strip().split(',') for i in f.readlines()]


async def fetch(session, url):
    while True:
        try:
            async with session.get(url) as resp:
                text = await resp.text()
                if TQDM_BAR:
                    TQDM_BAR.update(1)
                return text, url
        except Exception as e:
            print('Retrying...', url, e)
            await asyncio.sleep(1)


async def fetch_all(session, urls):
    return await asyncio.gather(
        *[asyncio.create_task(fetch(session, url)) for url in urls])


async def main():
    global TQDM_BAR

    data = read_list()
    urls = [i[-1] for i in data]

    results = []
    async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(30)) as session:
        TQDM_BAR = tqdm(total=len(urls))
        htmls = await fetch_all(session, urls)

        TQDM_BAR.close()
        print('done: ', len(htmls))
        for html, url in htmls:
            root = etree.HTML(html)
            result = {'url': url}
            for tr in root.xpath('//tbody[1]/tr'):
                if tr.xpath('th'):
                    key = tr.xpath('th')[0].text.strip()
                    value = tr.xpath('td/span')[0].text.strip() if tr.xpath(
                        'td/span')[0].text else ''
                    result[key] = value

            results.append(result)

        json.dump(results,
                  open('result.json', 'w'),
                  ensure_ascii=False, indent=4)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
