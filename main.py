import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://www.google.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup.title.string)


if __name__ == '__main__':
    main()
