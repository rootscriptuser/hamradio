from bs4 import BeautifulSoup
import requests
import sys
import json
import re

help="""
If no args are passed this help menu is displayed!

--fetch-v  # scrapes for VHF repetitors as html
--fetch-d  # scrapes for digi voice repetitors as html
--fetch-u  # scrapes for UHF repetitors as html

--parse-v
--parse-d
--parse-u
"""
args = sys.argv[1:]

if not args:
	raise SystemExit(print(help))


#54unc = requests.get("https://s54unc.eu.org/s5rpt")


if args[0] == "--fetch-v":
	s5rpt_2m = requests.get("https://rpt.hamradio.si/?modul=repetitorji&vrsta=2")
	with open("s5rpt-vhf.html", "w") as vhf:
		vhf.write(s5rpt_2m.text)
		vhf.close()

if args[0] == "--fetch-d":
	s5rpt_dv = requests.get("https://rpt.hamradio.si/?modul=repetitorji&vrsta=5")
	with open("s5rpt-dv.html", "w") as dv:
		dv.write(s5rpt_dv.text)
		dv.close()

if args[0] == "--fetch-u":
	s5rpt_uhf = requests.get("https://rpt.hamradio.si/?modul=repetitorji&vrsta=3")
	with open("s5rpt-uhf.html", "w") as uhf:
		uhf.write(s5rpt_uhf.text)
		uhf.close()

if args[0] =="--parse-v":
				with open("./s5rpt-vhf.html") as file:
						soup = BeautifulSoup(file, 'html.parser')

				all = soup.find('tbody')

				all = soup.find_all('tr')

				list_of_rpt=[]

				for tr in all:
					if tr.contents[3]:
						IN=tr.contents[3].text
					else:
						IN=''
					if tr.contents[5]:
						OUT=tr.contents[5].text
					else:
						OUT=''
					if tr.contents[9]:
						LOC=tr.contents[9].text
					else:
						LOC=''
					if tr.contents[13]:
						CTCSS=tr.contents[13].text
						CTCSS=CTCSS.strip()
						CTCSS=re.search("\d+.\d",CTCSS)
						if CTCSS == None:
							CTCSS=''
						else:
							CTCSS=CTCSS.group()	
					else:
						CTCSS=''
					if tr.contents[11]:
						UL=tr.contents[11].text
					else:
						UL=''
					if tr.contents[7]:
						CALL=tr.contents[7].text
					else:
						CALL=''
					UL = re.sub("[^a-zA-Z0-9_' ]+", '',UL)
					UL = UL[:-4]
					rpt = {"IN" : "", "OUT": "", "LOC":"", "CC": "","CALL":"", "UL":"","CTCSS":""}
					rpt["IN"]=str(IN).strip()
					rpt["OUT"]=str(OUT).strip()
					rpt["LOC"]=str(LOC).strip()
					rpt["UL"]=str(UL).strip()
					rpt["CALL"]=str(CALL).strip()
					rpt["CTCSS"]=str(CTCSS)
					list_of_rpt.append(rpt)
				with open("s5rpt-vhf.json", "w") as jeson:
					json.dump(list_of_rpt,jeson,indent=4)


if args[0] =="--parse-u":
				with open("./s5rpt-uhf.html") as file:
						soup = BeautifulSoup(file, 'html.parser')

				all = soup.find('tbody')

				all = soup.find_all('tr')

				list_of_rpt=[]

				for tr in all:
					if tr.contents[3]:
						IN=tr.contents[3].text
					else:
						IN=''
					if tr.contents[5]:
						OUT=tr.contents[5].text
					else:
						OUT=''
					if tr.contents[9]:
						LOC=tr.contents[9].text
					else:
						LOC=''
					if tr.contents[13]:
						CTCSS=tr.contents[13].text
						CTCSS=CTCSS.strip()
						CTCSS=re.search("\d+.\d",CTCSS)
						if CTCSS == None:
							CTCSS=''
						else:
							CTCSS=CTCSS.group()	
					else:
						CTCSS=''
					if tr.contents[11]:
						UL=tr.contents[11].text
					else:
						UL=''
					if tr.contents[7]:
						CALL=tr.contents[7].text
					else:
						CALL=''
					UL = re.sub("[^a-zA-Z0-9_' ]+", '',UL)
					UL = UL[:-4]
					rpt = {"IN" : "", "OUT": "", "LOC":"", "CC": "","CALL":"", "UL":"","CTCSS":""}
					rpt["IN"]=str(IN).strip()
					rpt["OUT"]=str(OUT).strip()
					rpt["LOC"]=str(LOC).strip()
					rpt["UL"]=str(UL).strip()
					rpt["CALL"]=str(CALL).strip()
					rpt["CTCSS"]=str(CTCSS)
					list_of_rpt.append(rpt)
				with open("s5rpt-uhf.json", "w") as jeson:
					json.dump(list_of_rpt,jeson,indent=4)

if args[0] =="--parse-d":
				with open("./s5rpt-dv.html") as file:
						soup = BeautifulSoup(file, 'html.parser')

				all = soup.find('tbody')

				all = soup.find_all('tr')

				list_of_rpt=[]

				for tr in all:
					if tr.contents[3]:
						IN=tr.contents[3].text
					else:
						IN=''
					if tr.contents[5]:
						OUT=tr.contents[5].text
					else:
						OUT=''
					if tr.contents[9]:
						LOC=tr.contents[9].text
					else:
						LOC=''
					if tr.contents[13]:
						CTCSS=tr.contents[13].text
						CTCSS=CTCSS.strip()
						CTCSS=re.search("\d+.\d",CTCSS)
						if CTCSS == None:
							CTCSS=''
						else:
							CTCSS=CTCSS.group()	
					else:
						CTCSS=''
					if tr.contents[11]:
						UL=tr.contents[11].text
					else:
						UL=''
					if tr.contents[7]:
						CALL=tr.contents[7].text
					else:
						CALL=''
					UL = re.sub("[^a-zA-Z0-9_' ]+", '',UL)
					UL = UL[:-4]
					rpt = {"IN" : "", "OUT": "", "LOC":"", "CC": "","CALL":"", "UL":"","CTCSS":""}
					rpt["IN"]=str(IN).strip()
					rpt["OUT"]=str(OUT).strip()
					rpt["LOC"]=str(LOC).strip()
					rpt["UL"]=str(UL).strip()
					rpt["CALL"]=str(CALL).strip()
					rpt["CTCSS"]=str(CTCSS)
					list_of_rpt.append(rpt)
				with open("s5rpt-dv.json", "w") as jeson:
					json.dump(list_of_rpt,jeson,indent=4)
