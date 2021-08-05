import requests
import sys
import time


class bColors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'


def banner():
    print(bColors.BLUE + '<<< Subdomain-Crawler v2.0 >>>')
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


class subdomainCrawler:
    def __init__(self):
        self.r = bColors.RED
        self.g = bColors.GREEN
        self.b = bColors.BLUE
        self.y = bColors.YELLOW

    def request(self, url):
        try:
            return requests.get("http://" + url)
        except requests.exceptions.ConnectionError:
            pass

    def print_links(self, target_url):
        try:
            subdomains = []
            with open("subdomains.txt", 'r') as file:
                for line in file:
                    word = line.strip()
                    test_url = word + "." + target_url
                    response = self.request(test_url)
                    subdomains.append("https://" + test_url)
                    test_url = 'https://' + test_url
                    sys.stdout.write(self.y + '\r' + '[' + self.g + '↻' + self.y + ']' + f' Checking {test_url}')
                    time.sleep(0.02)

                    if response:
                        print(self.b + '\r' + '[' + self.y + '+' + self.b + ']' + self.y +
                              f' Subdomain {test_url} exists !!')

            with open("subdomains.csv", "r+") as f:
                f.writelines(f'\n{target_url}, {subdomains}')

        except Exception as e:
            print(self.r + f'[-] ERROR: {e}')


if __name__ == '__main__':
    banner()
    sc = subdomainCrawler()
    targetUrl = input(bColors.BLUE + "Enter site for subdomain crawling (e.g. google.com): ")
    sc.print_links(targetUrl)
