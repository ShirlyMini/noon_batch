import pytest


@pytest.fixture()
def setup():
    print("this is setup")
    yield True
    print("this is teardown")

@pytest.fixture(scope="class")
def setup_class():
    print("this is setup CLASS")
    yield
    print("this is teardown CLASS")

@pytest.fixture(scope="module")
def setup_module():
    print("this is setup MODULE")
    yield
    print("this is teardown MODULE")


###
def pytest_configure(config):
    config.addinivalue_line("markers", "sanity: this is a tag name for sanity test cases")
    config.addinivalue_line("markers", "regression: this is a tag name for regression test cases")
