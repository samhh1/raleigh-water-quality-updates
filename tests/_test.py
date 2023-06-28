import src.utils as utils


def test_test_func():
    assert utils.test_func(1) == 2


def test_good_url():
    utils.extract_most_recent_raleigh_water_data("May", "23")


def test_already_posted_update():
    pass
