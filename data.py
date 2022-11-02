from requests import get

class Data:
    def __init__(self, url: str) -> None:
        self.url = url
        self.data = self._get_data()

    def _get_data(self) -> list:
        """Get data from the API"""
        try:
            res = get(self.url)
            return res.json()
        except Exception as e:
            print(e)
            return None

    def sort_by(self, key: str) -> list:
        """Sort data by key"""
        return sorted(self.data, key=lambda x: x[key])