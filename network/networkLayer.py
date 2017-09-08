import urllib.parse
import urllib.request
import json


class AbstractNetworkLayer:

    def get(self, path):
        pass

    def put(self, path):
        pass


class NetworkLayer(AbstractNetworkLayer):

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def get(self, path):
        url = urllib.parse.urljoin(self.endpoint, path)
        request = urllib.request.Request(url=url, method="GET")
        return json.loads(urllib.request.urlopen(request).read().decode())

    def put(self, path):
        url = urllib.parse.urljoin(self.endpoint, path)
        request = urllib.request.Request(url=url, method="PUT")
        urllib.request.urlopen(request).read().decode()
