import pytest
import logging


@pytest.fixture()
def dummy_data():
    return dict(user_id=123, sales="apple", quantity=400, price=1.12)


@pytest.fixture()
def demo_yield():
    logging.info("setting up based on demo yield")
    dummy_func = lambda x: x ** 2  # noqa
    yield dummy_func
    logging.info("tearing down based on demo yield")


@pytest.fixture()
# @pytest.fixture(autouse=True)
def function_fixture():
    logging.info("function trigger")
    return True


@pytest.fixture(scope="class")
def class_fixture():
    logging.info("class trigger")
    return True


@pytest.fixture(scope="module")
def module_fixture():
    logging.info("module trigger")
    return True


@pytest.fixture(scope="session")
def session_fixture():
    logging.info("session trigger")
    return True
