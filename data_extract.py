
import json
from utils import jsonutils




class DataExtract():
    def data_extract(self , soup):
        # This function is used to extract the data of a google lens page

        script_elements = soup.find_all('script')

        raw_data = [x for x in script_elements if 'Visual matches' in x.text]

        raw_data = raw_data[0].text

        start = raw_data.find('data:')+5
        end = raw_data.find('sideChannel') -2
        json_data = json.loads(raw_data[start:end])

        jason = []

        ###########################################
        # This is used beacuse sometimes the information is in json_data[1][0] and other times in json_data[1][1]
        try:
            jason = json_data[1][1][1][8][8][0][12] if len(json_data[1]) == 2 else json_data[1][0][1][8][8][0][12]
        except:
            print("The data is not in the expected format")
        ###########################################

        product_list = []
        # you can customize object attrs as your need
        for product in jason[0:19]:
            url = product[0][0]
            information = {
                'google_image': url,
                'image_bytes':jsonutils.image_to_json(url),
                'base_website': product[5],
                'image-name':product[3],
                'redirect-name' : product[14]
            }
            product_list.append(information)

        return product_list

data_extract= DataExtract()