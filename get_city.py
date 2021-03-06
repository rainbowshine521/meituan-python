import requests
import re
import json
from requests.exceptions import RequestException
import time

def get_city(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        return None
    except RequestException:
        return None


def get_city_parse(html):
    pattern = re.compile('<li.*?react.*?select.*?href="(.*?)".*?>(.*?)</a>', re.S)
    #pattern = re.compile('<h4.*?A.*?href="(.*?)".*?>(.*?)</a>', re.S)
    results = re.findall(pattern, html)
    for result in results:
        yield{
            'url': result[0],
            'city_name': result[1]
        }

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main():
    for i in range(65,91):
        url = 'http://i.meituan.com/index/changecity/more/' + chr(i) + '?cevent=imt%2FselectCity%2Fmore'
        html = get_city(url)
        #print(html)
        for item in get_city_parse(html):
            #print(item)
            write_to_file(item)

if __name__ == '__main__':
    main()
    time.sleep(1)

# print(type(r.text))
# print(r.text)
# print(type(r))
# print(r.status_code)