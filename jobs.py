from bs4 import BeautifulSoup
import requests
r=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
soup=BeautifulSoup(r.content,'html.parser')
jobs=soup.find_all('h3',class_="joblist-comp-name")
skills=soup.find_all('ul',class_="list-job-dtl clearfix")
locations=soup.find_all('ul',class_="top-jd-dtl clearfix")
info=soup.header.h2.a['href']
j=[]
s=[]
l=[]
for job in jobs:
    j.append(job.text.replace(" ",''))
for skill in skills:
    s.append(skill.text.replace(" ",''))
for loc in locations :
    l.append(loc.text.replace(" ",''))
print("_______________________________________________________________________________________________")
for i in range (0,len(j)):
    print("Company name : "+j[i].strip())
    print(s[i])
    print(l[i])
    print("___________________________________________________________________________________________")


