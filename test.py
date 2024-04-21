# Олеся Соколова, 15-я когорта -Финальный проект. Инженер по тестированию плюс
import sender_stand_request


def test_get_order_creation():
    new_response = sender_stand_request.post_new_order()
    track_id = new_response.json()
    response = sender_stand_request.get_orders_track(str(track_id.get("track")))
    assert response.status_code == 200
    print(f"status code={response.status_code == 200}")
