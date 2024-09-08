import json
from typing import Dict

import requests


class SwapiApiConsumer:
    @classmethod
    def get_starships(self, page: int) -> Dict:
        params = {'page': page}

        req = requests.get('https://swapi.dev/api/starships/', params=params)

        res = json.loads(req.content)

        print(type(res))

        return res
