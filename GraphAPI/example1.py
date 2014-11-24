import facebook
import json

def pp(o):
    print json.dumps(o, indent=1)

def hd(s):
    print
    print ('-'*10)
    print s
    print ('-'*10)

g = facebook.GraphAPI(YOURTOKEN)

hd("Me")
pp(g.get_object('me'))
hd("My Friends")
pp(g.get_connections('me', 'friends'))
hd("Social Web")
pp(g.request("search",{'q': 'social web', 'type': 'page'}))
