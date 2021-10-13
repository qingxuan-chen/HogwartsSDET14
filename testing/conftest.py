import pytest


@pytest.fixture()
def login(request):
    print('登录方法')
    print(request.param)
    yield ['username', 'password']
    print('teardown')
