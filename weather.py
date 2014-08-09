from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import csv
import sys

f = open(sys.argv[1], 'wt')

url="http://panahon.observatory.ph/index.html"
page=urlopen(url)
soup = BeautifulSoup(page.read())

areas=soup.findAll('div',{'id':re.compile("\w*-rain$")})

try:
	writer = csv.writer(f)
	writer.writerow( ('Station', 'Timestamp', 'Rainfall') )
	for eacharea in areas:
		details = eacharea.findAll('span',{'class':'highlight'})
		writer.writerow(((eacharea.get('id')),(details[0].text),(details[1].text)))
finally:
	f.close()

print (open(sys.argv[1], 'rt').read())