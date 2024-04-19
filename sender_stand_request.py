import requests
import configuration
import data

def post_new_order():
    return requests.post(configuration.URL_SERVER + configuration.CREATE_NEW_ORDER,
                         json=data.order_body)
def get_info_track(track_id):
    return requests.get(configuration.URL_SERVER + configuration.GET_INFO_TRACK + str(track_id))
