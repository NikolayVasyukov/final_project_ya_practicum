import data
import sender_stand_request


def test_number_one_update():
    response_order = sender_stand_request.post_new_order(data.body_order)
    track = {"t": response_order.json()["track"]}
    track_resp = sender_stand_request.get_order_by_track(track)


    assert track_resp.status_code == 200
