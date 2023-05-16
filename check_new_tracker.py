import data
import sender_stand_request


def test_possitive_assert(): # Пока сам не понял что это :)
    body_track = sender_stand_request.get_new_order(track_id)
    track_response = "t=" + sender_stand_request.get_order_by_track(body_track)

    assert track_response.status_code == 200


def test_number_one():
    track_number = "t=" + sender_stand_request.get_new_order()
