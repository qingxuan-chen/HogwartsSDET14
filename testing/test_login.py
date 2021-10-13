import pytest


# @pytest.fixture()
# def login():
#     print('登录方法')
#     yield ['username', 'password']
#     print('teardown')

@pytest.mark.parametrize('login', [('user3', 'password3'), ('user4', 'password4')], indirect=True)
@pytest.mark.parametrize('a, b', [(1, 2), (3, 4)])
def test_case1(login, a, b):
    print(f'case1 login = {login}')


def test_case2():
    print('case2')


def test_case3():
    print('case3')
