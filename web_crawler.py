import requests
import re
from urllib.parse import urljoin
import sys


class bColors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'


def banner():
    print(bColors.BLUE + '<<< Web-Crawler v2.0 >>>')
    print(bColors.YELLOW + r'''
  _
 | |
 | |___
 |  _  \   _   _
 | |_)  | | (_) |
  \____/   \__, |
            __/ |
           |___/
                                       _                                                         _
                                      | |                                                       (_)
                  ____    ____     ___| |   ___ _   ______   ______    ___ _   ______   ______   _   _ ____
                 / ___\  /    \   /  _  |  / _ | | /  ____| /  ____|  / _ | | /  ____| /  ____| | | | |   | \
                | |____ |  ()  | |  (_| | | (_|| | \_____ \ \_____ \ | (_|| | \_____ \ \_____ \ | | | |   | |
                 \____/  \____/   \____/   \___|_| |______/ |______/  \___|_| |______/ |______/ |_| |_|   |_|
     ''')


class webCrawler:

    def __init__(self):
        self.response = None
        self.r = bColors.RED
        self.g = bColors.GREEN
        self.b = bColors.BLUE
        self.y = bColors.YELLOW

    def extract_links(self, url):
        try:
            print(self.y + '[+] Extracting links ...\n')
            self.response = requests.get(url)
            linkList = re.findall('(?:href=")(.*?)"', self.response.content.decode('utf8'))
            print(self.g + '[+] Link extraction successful !!\n')
            return linkList

        except Exception as e:
            print(self.r + f'[-] ERROR: {e}')
            sys.exit(0)


def print_links(href_link, target_url):
    try:
        print(bColors.BLUE + '[+] Printing links...\n')
        for link in href_link:
            link = urljoin(target_url, link)
            print(bColors.YELLOW + '[+] ' + link)

    except Exception as e:
        print(bColors.RED + f'[-] ERROR: {e}')
        sys.exit(0)


if __name__ == '__main__':
    banner()
    wc = webCrawler()
    targetUrl = 'http://' + input(bColors.BLUE + 'Enter a website for crawling: ')
    hrefLink = wc.extract_links(targetUrl)
    print_links(hrefLink, targetUrl)
