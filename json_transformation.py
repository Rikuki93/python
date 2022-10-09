import json
from transformation import Transformation


class JSONTransformation(Transformation):
    def transform(self, data):
        json_data = json.dumps(data)
        return json.loads(json_data)
