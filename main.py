import os
import requests
from bs4 import BeautifulSoup
import re
import json
import time
#creating folder to save the wallpapers
path="wallpapers"
#checks if the folder already exists
if os.path.exists(path)==False:
    os.mkdir(path)
    print(f'{path} folder created')
else:
    print(f'{path} folder already exists')

def search():

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
    img_names=[]
    img_url=[]
    wall_url_ls=[]
    img_tags=soup.find_all('img',alt='loading')
    for i in range(len(img_tags)):
        split_url=str(img_tags[i]).replace('"','').split()[3].split('=')[1]
        img_names.append(str(split_url).replace('.jpg','').split('/')[-1])

    for i in img_names:
        res=requests.get(f'https://wallhaven.cc/w/{i}')
        soup=BeautifulSoup(res.content,'html5lib')
        wall_url_find=soup.find_all('img',id="wallpaper")
        if wall_url_find:
            wall_url=str(wall_url_find).split('"')[-2]
            wall_url_ls.append(wall_url)
        else:
            continue
    #Saves the wallpapers
    for i in wall_url_ls:
        response=requests.get(i)
        filename = word+os.path.basename(i)
        folder='wallpapers'
        file_path=os.path.join(folder,filename)
        if response.status_code==200:
            print("Downloading : %s " % (filename))
            with open(file_path,'wb') as file:
                file.write(response.content)
                time.sleep(5)
        else:
            print('response 200 not received')

def main():
    print('How do you want to get your wallpapers?')
    while True:
        ask=int(input('Press 1 for direct search :'))
        if ask==1:    
            search()
            break
        else:
            print('Enter valid input')    
        

main()

