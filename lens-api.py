from fastapi import FastAPI ,Request
import bs4, requests
from data_extract import data_extract
from utils import jsonutils
"""
to run application
install requrement.txt
run terminal in lens-api.py directory
start uvicorn using $uvicorn lens-api:app --reload
use service by serverip:8000/image-link

"""




# create api in root directory
app = FastAPI()
@app.get('/{_:path}')
def pred_image(request: Request):

    url = 'https://lens.google.com/uploadbyurl?url='+request.url.path[1:]
    session = requests.session()
    google_page = session.get('https://google.com' , headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0'})
    google_response_headres = dict(google_page.headers)
    # set cookie for using google_lens service
    google_cookie = google_response_headres.get('Set-Cookie')
    page = requests.get(url=url , 
                        allow_redirects=True ,
                        headers={'cookie':google_cookie
                            , 'referer' : 'https://www.google.com/' , 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0'})
    if page.status_code != 200:
        return f'cant access to google lens services maybe you blocked by host error code = {page.status_code} '
    soup = bs4.BeautifulSoup(page.text , 'html.parser')
    img_data = data_extract.data_extract(soup=soup)
    
    
    #  use this for loop for save image as .jpg to local disk
    # for counter , data in enumerate(img_data):
    #   jsonutils.json_to_image(data.get('image_bytes') , counter)
    
    
    return img_data



