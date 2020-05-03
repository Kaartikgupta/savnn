from bs4 import BeautifulSoup
import requests
choice={'1':'LdbVc1Z5i9E_',
        '2':'8MT-LQlP35c_',
        '3':'W6DUe-fP3X8_'}
ch=input("press 1 for English \n 2 for Hindi \n 3 for Punjabi")
res=requests.get('https://www.jiosaavn.com/featured/weekly-top-songs/'+choice[ch])

soup=BeautifulSoup(res.text,'lxml')

song=soup.find('ol',{'class':'content-list'})
song_all=song.find_all('div',{'class':'details'})

for i,s in enumerate(song_all,1):
    song_all1=s.find('p',{'class':'song-name'})
    print(i,song_all1.text)