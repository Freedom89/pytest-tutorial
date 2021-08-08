import pytest
import logging


@pytest.fixture(scope="function", autouse=True)
def function_autouse():
    logging.info("scope: function autouse")


@pytest.fixture(scope="function")
def function():
    logging.info("scope: function")


@pytest.fixture(scope="class", autouse=True)
def class__autouse():
    logging.info("scope: class autouse")


@pytest.fixture(scope="class")
def class_():
    logging.info("scope: class")


@pytest.fixture(scope="module", autouse=True)
def module_autouse():
    logging.info("scope: module autouse")


@pytest.fixture(scope="module")
def module():
    logging.info("scope: module")


@pytest.fixture(scope="package", autouse=True)
def package_autouse():
    logging.info("scope: package autouse")


@pytest.fixture(scope="package")
def package():
    logging.info("scope: package")


@pytest.fixture(scope="session", autouse=True)
def session_autouse():
    logging.info("scope: session autouse")


@pytest.fixture(scope="session")
def session():
    logging.info("scope: session")


def test_order(module, class_, session, function, package):
    assert True
