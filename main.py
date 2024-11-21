import os
import requests
from bs4 import BeautifulSoup
import re
import json
#creating folder to save the wallpapers
def folder():
    path="wallpapers"
    #checks if the folder already exists
    if os.path.exists(path)==False:
        os.mkdir(path)
        print(f'{path} folder created')
    else:
        print(f'{path} folder already exists')

def main():
    #folder()
    while True:
        word=input('Enter what type of wallpaper you want (keyword): ')
        if word.isdigit()==True:
            print('Enter a valid input')
        else:
            print(word)
            break
    URL=f"https://wallhaven.cc/search?q={word}"
    r=requests.get(URL)
    soup=BeautifulSoup(r.content,'html5lib')
    img_url=[]
    #img_tags=[]
    img_tags=soup.find_all('img',alt='loading')
    #print(img_tags)
    for i in range(len(img_tags)):
        #for j in range(len(img_tags)):
        split_url=str(img_tags[i]).replace('"','').split()[3].split('=')[1]
        print('split_url',split_url)
        img_url.append(split_url)
        print('append done')
        #split=str(split).split()
        #img_url.append(split.replace('data-src=',''))
        #img_url.append(split[3])
        #print(split)
    print(img_url[1])
    # print(img_url)
    #     img_link=img_tags.find('data-src')
    #     img_url.append(img_link)
    # print(img_tags)
    #print(img_url)
    # print(str(img_tags[1]).split('https'))    
   
    #print(str(img_tags[1]).split('https'))    
    
main()

