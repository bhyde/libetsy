from etsy import Etsy, getAll
from os import environ

e = Etsy(environ.get("ETSY_API_KEY", "YOUR API KEY HERE"))

# get my Shop 
s = e.getShopDetails('mck254')

print "people who favor the shop %s" % s.user_name
print

#iterate through people that favorite me:
for f in s.getFavorers():
    if f.status != 'private':
        print f.user_name

print
print "%s's listings" % s.user_name
print

#iterate through my listings
for l in s.getListings():
    print l.title


#Now, let's get all the mike's on etsy

mikes = getAll(e.getUsersByName, search_name='mike')

print "We found %d Mikes" % len(mikes)
