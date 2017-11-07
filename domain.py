from urllib.parse import urlparse

def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')       #result is a list
        return results[-2] + '.' + results[-1]
    except:
        return ''

#getting the subdomain name (xyz.name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc     #return the network location
    except:
        return ''
