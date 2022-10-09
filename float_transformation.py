import json
from transformation import Transformation


class FloatTransformation(Transformation):
    def transform(self, data):
        json_data = json.dumps(data)
        res = json.loads(json_data)
        return float(res["income"])


