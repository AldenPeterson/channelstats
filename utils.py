#! /usr/bin/env python2.7

import decimal
import json

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


def jdump(j):
    """
    json.dumps(j), but deal with Decimal encoding
    """
    return json.dumps(j, indent=4, cls=DecimalEncoder)