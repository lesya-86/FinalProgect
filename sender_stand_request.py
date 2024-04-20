import requests
import configuration
import data

def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                         json=data.order_body)
def get_info_track(track_id):
    get_info_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_id}"
    response = requests.get(get_info_url)
    return response
    return requests.get(configuration.URL_SERVICE + configuration.GET_INFO_TRACK + str(track_id))


