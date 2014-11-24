import facebook
import json

def pp(o):
    print json.dumps(o, indent=1)

def int_fmt(n): return "{:,}".format(n) 

g = facebook.GraphAPI(YOURTOKEN)

pepsi    = g.request('search', {'q':'pepsi','type':'page','limit':1})
pepsi_id = pepsi["data"][0]["id"]
coke     = g.request('search', {'q':'coke','type':'page','limit':1})
coke_id  = coke["data"][0]["id"]

print "Pepsi likes:", int_fmt(g.get_object(pepsi_id)['likes'])
print "Coke  likes:", int_fmt(g.get_object( coke_id)['likes'])


