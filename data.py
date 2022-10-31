from requests import get

class Data:
    def __init__(self, url: string):
        self.url = url
        self.data = self._get_data()

    def _get_data():
        try:
            res = get(self.url)
            return res.json()
        except:
            raise RequestError