# import pytest


# @pytest.fixture()
# def login():
#     print('登录方法')
#     yield ['username', 'password']
#     print('teardown')


def test_case1(login):
    print(f'case1 login = {login}')


def test_case2():
    print('case2')


def test_case3():
    print('case3')
