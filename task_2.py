import requests

YA_TOKEN = 'y0_AgAAAAAH2mLYAADLWwAAAADWlCWcN2c_iTa1S-ahghdFUGRcyhpgubk'


class YaDisk:

    def __init__(self, ya_token):
        self.ya_token = ya_token
        self.ya_host = 'https://cloud-api.yandex.net:443'
        self.headers = {'Authorization': f'OAuth {self.ya_token}'}

    def create_folder(self, path):
        uri = '/v1/disk/resources'
        response = requests.put(
            self.ya_host + uri + '?path=' + path, headers=self.headers)
        return response.status_code

    def get_metainfo(self, path):
        uri = '/v1/disk/resources'
        response = requests.get(
            self.ya_host + uri + '?path=' + path, headers=self.headers)
        return response.status_code
