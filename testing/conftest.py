import pytest


@pytest.fixture()
def login():
    print('登录方法')
    yield ['username', 'password']
    print('teardown')
