import urllib3
import re

visited = []

def navigator(url,head,handle):
    visited.append(url)
    r = handle.request('GET', url)
    print (url,":")
    print (r.data.decode('utf-8'))
    t =  r.data.decode('utf-8')
    helper = r"href=\"(\S+)"
    if re.search(helper, t):
        m = re.search(helper, t)

        print ()
        print (m)
        print (m.group(1))
    else:
        print ("No links found!")
    #if already visited skip
    #if not add to head call navigator



urlprey = "https://www.lainchan.org"

handle = urllib3.PoolManager()
navigator(urlprey,urlprey,handle)

