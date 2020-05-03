from bs4 import BeautifulSoup
import requests

res=requests.get('https://www.jiosaavn.com/featured/weekly-top-songs/8MT-LQlP35c_')

soup=BeautifulSoup(res.text,'lxml')

song=soup.find('ol',{'class':'content-list'})
song_all=song.find_all('div',{'class':'details'})

for i,s in enumerate(song_all,1):
    song_all1=s.find('p',{'class':'song-name'})
    print(i,song_all1.text)