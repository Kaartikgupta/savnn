from bs4 import BeautifulSoup
import requests
choice={'1':'LdbVc1Z5i9E_',
        '2':'8MT-LQlP35c_',
        '3':'W6DUe-fP3X8_'}

def print_choice():
    for sno in sorted(choice):
        print('{}. {}'.format(sno,choice[sno]))
    ch=input('Enter your choice[1-5]')
    return choice[ch]

def get_song(lang):

    res=requests.get('https://www.jiosaavn.com/featured/weekly-top-songs/'+lang)

    soup=BeautifulSoup(res.text,'lxml')

    song=soup.find('ol',{'class':'content-list'})
    song_all=song.find_all('div',{'class':'details'})
    return song_all
def print_song(song_all):
    for i,s in enumerate(song_all,1):
        song_all1=s.find('p',{'class':'song-name'})
        print(i,song_all1.text)
def saavn():
    lang=print_choice()
    song_all=get_song(lang)
    print_song(song_all)

saavn()