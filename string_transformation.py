import json
from transformation import Transformation


class StringTransformation(Transformation):
    def transform(self, data):
        json_data = json.dumps(data)
        res = json.loads(json_data)
        return str(res["income"]) + " is a string"
