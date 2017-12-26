import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin

ignorewords = set(['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it'])


class crawler:
    def __init__(self, dbname):
        pass

    def __del__(self):
        pass

    def dbcommit(self):
        pass

    def getentryid(self, table, field, value, createNew=True):
        return None

    def addtoindex(self, url, soup):
        print('Index %s' % url)

    def gettextonly(self, soup):
        return None

    def seperatewords(self, text):
        return None

    def isindexed(self, url):
        return False

    def addlinkref(self, urlFrom, urlTo, linkText):
        pass

    def crawl(self, pages, depth=2):
        for i in range(depth):
            newpages = set()
            for page in pages:
                try:
                    c = urllib.request.urlopen(page)
                except:
                    print("Couldn't open %s" % page)
                    continue
                soup = BeautifulSoup(c.read(), "html.parser")
                self.addtoindex(page, soup)

                links = soup('a')
                for link in links:
                    if 'href' in dict((link.attrs)):
                        url = urljoin(page, link['href'])
                        if url.find("'") != -1:
                            continue
                        url = url.split("#")[0]
                        if url[0:4] == 'http' and not self.isindexed(url):
                            newpages.add(url)
                        linkText = self.gettextonly(link)
                        self.addlinkref(page, url, linkText)
                self.dbcommit()
                pages = newpages

    def createindextables(self):
        pass


pageList = ['https://en.wikipedia.org/wiki/Wikipedia']
crawler = crawler('')
print(crawler.crawl(pageList))
