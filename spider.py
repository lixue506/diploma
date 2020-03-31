import requests
from bs4 import BeautifulSoup

def get_html(url):
    d = {'User Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
    r = requests.get(url, params=d )
    if r.status_code == 200:
        return r.text

def parse_html(html):
    soup = BeautifulSoup(html, "lxml")
    data = soup.body.find('tr',{'class':"topline"})
    for i in data.next_siblings:
        for j in i.find_all('td'):
            print(j.text)

if __name__ == "__main__":
    url = 'http://chuangshi.qq.com/bang/mo/'
    html = get_html(url)
    parse_html(html)


