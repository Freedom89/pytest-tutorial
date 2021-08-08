import pytest
import logging


def test_calculate_sales_volume(dummy_data):
    logging.info("this is to demostrate that the logging does not print out")
    assert dummy_data.get("user_id") == 123


@pytest.mark.special
def test_special_marker(dummy_data):
    logging.info("special marker test")
    assert dummy_data.get("user_id") == 123


def test_yield(demo_yield):
    my_func = demo_yield  # yield the function
    assert my_func(10) == 100
    logging.info("this is to demostrate its still happening in this test function")
