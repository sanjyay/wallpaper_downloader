import os
#creating folder to save the wallpapers
path="wallpapers"
#checks if the folder already exists
if os.path.exists(path)==False:
    os.mkdir(path)
    print(f'{path} folder created')
else:
    print(f'{path} folder already exists')

def main():
    while True:
        word=input('Enter what type of wallpaper you want (keyword): ')
        if word.isdigit()==True or len(word.split())>1:
            print('Enter a valid input')
        else:
            print(word)
            break
main()

