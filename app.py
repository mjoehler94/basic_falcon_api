import falcon

from timestamp import TimeStamp

api = application = falcon.API()

timestamp = TimeStamp()

api.add_route('/timestamp', timestamp)
