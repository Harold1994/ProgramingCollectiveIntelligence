import urllib.request
import xml.dom.minidom

import time

kayakkey='YOURKEYHere'
def getkayaksession():
    url = 'http://www.kayak.com/k/ident/apisession?token=%s&version=1' % kayakkey
    doc = xml.dom.minidom.parseString(urllib.request.urlopen(url).read())
    sid = doc.getElementsByTagName('sid')[0].firstChild.data
    return sid

def flightsearch(sid,origin,destination,depart_date):

    url = 'http://www.kayak.com/s/apisearch?basicmode=true&oneway=y&origin=%s' % origin
    url += '&destination=%s&depart_date=%s' % (destination, depart_date)
    url += '&return_date=none&depart_time=a&return_time=a'
    url += '&travelers=1&cabin=e&action=doFlights&apimode=1'
    url += '&_sid_=%s&version=1' % (sid)

    doc = xml.dom.minidom.parseString(urllib.request.urlopen(url).read())
    searchid = doc.getElementsByTagName('serarchid')[0].firstChild.data
    return searchid

def flightsearchresults(sid,searchid):
    def parceprice(p):
        return float(p[1:].replace(',',''))
    while 1:
        time.sleep(2)
        url = 'http://www.kayak.com/s/basic/flight?'
        url += 'searchid=%s&c=5&apimode=1&_sid_=%s&version=1' % (searchid, sid)
        doc=xml.dom.minidom.parseString(urllib.request.urlopen(url).read())

        morepending = doc.getElementsByTagName('morepending')[0].firstChild
        if morepending == None or morepending.data=='false':
            break
    url = 'http://www.kayak.com/s/basic/flight?'
    url += 'searchid=%s&c=999&apimode=1&_sid_=%s&version=1' % (searchid, sid)
    doc = xml.dom.minidom.parseString(urllib.request.urlopen(url).read())

    prices = doc.getElementsByTagName('price')
    departures = doc.getElementsByTagName('depart')
    arrivals=doc.getElementsByTagName('arrive')

    return zip([p.firstChild.data.split(' ')[1] for p in departures],
               [p.firstChild.data.split(' ')[1] for p in arrivals],
                [p.firstChild.data.split(' ')[1] for p in prices])