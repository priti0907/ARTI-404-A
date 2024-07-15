import streamlit as st
import requests
from bs4  import BeautifulSoup
import pandas as pd

webpage=requests.get(f'https://www.scrapethissite.com/pages/forms/').text
soup=BeautifulSoup(webpage,features='lxml')
players=soup.find_all('tr')[1:]
#print(players)
team_name=[]
year=[]
win=[]
losses=[]
for i in players:
    name=i.find_all('td')[0].text.strip()
    yr=i.find_all('td')[1].text.strip()
    wn=i.find_all('td')[2].text.strip()
    ls=i.find_all('td')[3].text.strip()
    team_name.append(name)
    year.append(yr)
    win.append(wn)
    losses.append(ls)
data=pd.DataFrame({'Team name':team_name,"year":year,'wins':win,'losses':losses})

print(data)
st.dataframe(data)
