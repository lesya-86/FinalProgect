import requests
import configuration
import data

def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                         json=data.order_body)
def get_orders_track(track_id):
    return requests.get(configuration.URL_SERVICE + configuration.GET_INFO_BY_TRACK + str(track_id))


