import base64
import requests

"""
use this module to convert jpg and json data to eachothers
"""

class JsonUtils():
    def json_to_image(self , data , file_name):
        try:
            decoded_data=base64.b64decode(data)
            # write the decoded data back to original format in  file
            img_file = open(f'{file_name}.jpeg', 'wb')
            img_file.write(decoded_data)
            img_file.close()
        except:
            return f'oops somtings went wrong'
    def image_to_json(self ,url):
        try:
            image = requests.get(url)
            return base64.encodebytes(image.content).decode('utf-8')
        except:
            return f'cant access to this file please download it manualy'

jsonutils = JsonUtils()