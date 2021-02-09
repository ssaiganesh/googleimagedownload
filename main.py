import os
import json
import requests
from bs4 import beautifulsoup

# user can input a topic and a number
# download first n images from google image search 
#current issue with code doesn't go above 80 images

GOOGLE_IMAGE = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

# The User-Agent request header contains a characteristic string 
# that allows the network protocol peers to identify the application type, 
# operating system, and software version of the requesting software user agent.
# needed for google search
#this was copied from another code. Not exactly sure of the details within yet
usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}


SAVE_FOLDER = 'images'
def main():
    if not os.path.exists(SAVE_FOLDER):
        os.mkdir(SAVE_FOLDER) #creates new folder for images

    download_images()

def download_images():
    data = input('what are you looking for? ')
    n_images = int(input('how many images do you want? '))

    print('start searching...')

    searchurl = GOOGLE_IMAGE + 'q=' + data
    print(searchurl)

    response = requests.get(searchurl, headers=usr_agent)
    html - response.text

    soup = BeautifulSoup(html, 'html.parser') 
    results = soup.findAll('img', class = "rg_i Q4LuWd", limit=n_images) #From the html code of the google images site

    imagelinks = []
    for result in results :
        text = result.text
        print(text)
        text_dict = json.loads(text)
        link = text_dict['ou'] #'ou has the link ; 'ity' : 'png'
        imagelinks.append(link)
    
    print(f'found {len(imagelinks)} images')
    print('start downloading....')
    for i , imagelink in enumerate(iamgelinks):
        response = requests.get(imagelink)

        iamgename = SAVE_FOLDER + '/' + data + str(i+1) + '.jpg'
        with open(imagename, 'wb') as file:
            file.write(response.content)
    
    print('Done.. ')


if __name__ == '__main__':
    main()

