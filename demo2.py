import sys
import requests
import time
from bs4 import BeautifulSoup

URL = "https://search.books.com.tw/search/query/key/{0}/cat/all"

def generate_search_url(url,keywork):
    url=url.format(keywork)
    return url

def get_resource(url):
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" 
        "AppleWebKit/537.36 (KHTML, like Gecko)" 
        "Chrome/89.0.4389.114 Safari/537.36"
        }
    return requests.get(url,headers=headers,verify=False)

def parse_html(r):
    if r.status_code == requests.codes.ok:
        r.encoding = "utf8"
        soup = BeautifulSoup(r.text,"lxml")
    else:
        print("HTTP request error..."+url)
        
        soup=None
    return soup

def web_scraping_bot(url):
    booklist=[]
    print("retrive data from Internet...")
    if soup!=None:
        tag_item=soup.find_all(class_="bd")
        #print(tag_item)
        for item in tag_item:
            book=[]
            book.append(item.find("img")["alt"])
            [isbn,price]=get_ISBN_Price(item.find("a")["href"])
            book.append(isbn)
            book.append(price)
            print(book)

            print("wait 2 sec")
            time.sleep(2)

def get_ISBN_Price(url):
    urll="https" + url
    print(urll)
    return [urll,'1000']

if __name__== "__main__":
    if len(sys.argv) > 1:
        url=generate_search_url(URL,sys.argv[1])
        #print(get_resource(url).text)
        booklist = web_scraping_bot(url)
        for item in booklist:
            print(item)