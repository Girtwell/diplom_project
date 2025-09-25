import requests


class SearchApi:
    base_url = "https://web-gate.chitai-gorod.ru/api/v2"

    def search(self, title: str):
        path = "{read_city}/search/facet-search?customerCityId=213&phrase={book}".format(read_city=self.base_url, book=title)

        cookie = {
            "access-token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTg5ODU1OTMsImlhdCI6MTc1ODgxNzU5MywiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6ImUxODgxMzE3ZjE5ZTNhZjU1OWU4N2Q1YzFjMjFjNWEyNmI4NTQxOTBlMzNjZTQyMzc2YjBhODc5YTFkNGIxMjYiLCJ0eXBlIjoxMH0.tUk5c1JHnZdlpFEy6zH_v0_0EGCP5CDrd1c1VH52D-g"
        }

        requests.get(path, cookies=cookie)
