import sender_stand_request


def test_number_one():
    new_track = sender_stand_request.get_new_order()
    track_resp = sender_stand_request.get_order_by_track(new_track)


    assert track_resp.status_code == 200

