'''
Created on Apr 19, 2014

@author: rajni
'''
import urllib
from bs4 import BeautifulSoup

urls = ["http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/West_Champaran.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/East Champaran.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Sheohar.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Sitamarhi.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Madhubani.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Supaul.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Araria.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Kishanganj.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Purnia.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Katihar.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Madhepura.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Saharsa.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Darbhanga.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Muzaffarpur.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Gopalganj.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Siwan.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Saran.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Vaishali.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Samastipur.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Begusarai.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Khagaria.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Bhagalpur.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Banka.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Munger.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Lakhisarai.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Sheikhpura.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Nalanda.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Patna.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Bhojpur.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Buxar.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Kaimur.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Rohtas.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Arwal.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Jehanabad.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Aurangabad.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Gaya.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Nawada.html",
        "http://ceobihar.nic.in/election/Assembly_Election_2010/EXPENDITURE/include/Jamui.html"]
textfile=open("C:\\Users\\rajni\\Documents\\bihar-assembly2010.txt","w")
for url in urls:
    page = urllib.urlopen(url)
    html = page.read()    
    soup=BeautifulSoup(html)
    table = soup.find('table',{'border':'1'})
    tr=table.findAll('tr')
    i=0
    while i<len(tr):
        textfile.write(tr[i].text)
        i+=1
textfile.close()
#print tBody
#print city