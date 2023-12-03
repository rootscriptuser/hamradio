from bs4 import BeautifulSoup
import re
import json


with open("./test.html") as file:
    soup = BeautifulSoup(file, 'html.parser')

all = soup.find('tbody')

all = soup.find_all('tr')

for tr in all:
    in_=tr.contents[1].text
    call=tr.contents[5].b.text
    out=tr.contents[3].text
    location=tr.contents[7].text
    sysop=tr.contents[13].text
    _ul=tr.contents[9].text
    ul = re.sub("[^a-zA-Z0-9_' ]+", '',_ul)
    ul = ul[:-4]
    xxx = {"IN" : "", "OUT": "", "LOCATION":"", "CC": "","CALL":"", "UL":"","CTSS":"123.0"}
    xxx["IN"]=str(in_)
    xxx["OUT"]=str(out)
    xxx["LOCATION"]=str(location)
    xxx["UL"]=str(ul)
#    xxx["CC"]=str(cc)
    xxx["CALL"]=str(call)
    xxy=json.dumps(xxx)
    print(xxy)
