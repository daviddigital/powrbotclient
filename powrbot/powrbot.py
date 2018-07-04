'''
Powrbot Client API
'''

import requests

class Powrbot:

    def __init__(self, secret_key, api=None):
        self.secret_key = secret_key
        self.api = api or 'https://powrbot.com/api/v1/'
        self.response = None
    
    def _get_headers(self, **kwargs):
        '''Returns headers for request
        '''
        headers = {'Authorization': 'secret-key {0}'.format(self.secret_key)}

        return headers

    def _get_url(self, resource):
        '''Get API endpoint URL formated
        '''
        url = "{0}/{1}/".format(self.api, resource)
        url = url.replace("//", "/").replace("http:/", "http://").replace(
            "https:/", "https://")
        return url

    def send(self, resource='search', method='GET', file=None, data={}):
        '''Sends API request on given end_point
        ::param resource:: API resource name e.g. search
        ::param file:: Path to CSV file to upload
        ::param params:: Additional data to send to server in dictionary format

        ::return JSON or Text
        '''
    
        kwargs = {
            'headers': self._get_headers()
        }
        if file:
            files = {'csv_file': open(file, 'rb')}
            kwargs['files'] = files
        
        if data:
            kwargs['data']= data

        if method.lower() == 'post':
            self.response = requests.post(self._get_url(resource), **kwargs)
        else:
            self.response = requests.get(self._get_url(resource), **kwargs)
            
        # if req.status_code <200 and req.status_code >=300:
        #     raise Exception("Error")
    
        try:
            return self.response.json()
        except:
            return self.response.text

