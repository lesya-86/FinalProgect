# Олеся Соколова, 15-я когорта -Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data


def test_order_creation():
    new_response = sender_stand_request.post_new_order()
    track_id = new_response.json()['track']
    response = sender_stand_request.get_info_track(track_id)
    assert response.status_code == 200
