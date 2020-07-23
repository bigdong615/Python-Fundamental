import urllib.request
import random
import json
url = 'http://www.whatismyid.com'
iplist = ['xxxx', 'xxxx']

proxy_support = urllib.request.ProxyHandler({'http', random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)

opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0')]

opener.open(url)
#urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)
