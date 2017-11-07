from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    #this is a function of HTMLParser...hey!!! by default it doesn't do anything but we're gonna override it...

    def handle_starttag(self, tag, attrs):      #attrs is basically a 'list of tuples' of attribute and value
        if tag == 'a':                          #this means if its a link(anchor)
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)   #convert relative url to full url
                    self.links.add(url)

    def page_links(self):
        return self.links

    #implement abstract methods...hey!!! that's a rule!!!
    def error(self, message):
        pass
