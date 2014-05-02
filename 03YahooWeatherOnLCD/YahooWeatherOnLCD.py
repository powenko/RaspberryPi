#!/usr/bin/python
# create by Powen Ko, www.powenko.com
import sys, getopt
import urllib
from xml.dom import minidom

WEATHER_URL = 'http://xml.weather.yahoo.com/forecastrss?u=c&w=%s'
WEATHER_NS = 'http://xml.weather.yahoo.com/ns/rss/1.0'

def weather_for_zip(zip_code):
    url = WEATHER_URL % zip_code
    dom = minidom.parse(urllib.urlopen(url))
    forecasts = ""
    for node in dom.getElementsByTagNameNS(WEATHER_NS, 'forecast'):
        forecasts.append({
                         'L': node.getAttribute('low'),
                         'H': node.getAttribute('high')
                         })
    ycondition = dom.getElementsByTagNameNS(WEATHER_NS, 'condition')[0]
    return {
        'Now': ycondition.getAttribute('text'),
        'C': ycondition.getAttribute('temp'),
        'forecasts': forecasts
    }
zipcode=2436704
if(len(sys.argv)>0):
    zipcode=sys.argv[1]
print weather_for_zip(zipcode)