import falcon
import json
# import arrow


class TimeStamp(object):

    def _init__(self):
        return

    def on_get(self, req, resp):
        payload = {}
        # payload['utc'] = arrow.utcnow().format('YYYY-MM-DD HH:mm:SS')
        # payload['unix'] = arrow.utcnow().timestamp
        payload['health'] = 'This is a health test sort of'

        # dumb the dictionary contents into the response body in json format
        resp.body = json.dumps(payload)
        resp.status = falcon.HTTP_200
        return

