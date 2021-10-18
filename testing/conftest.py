from typing import List

import pytest


@pytest.fixture()
def login(request):
    print('登录方法')
    print(request.param)
    yield ['username', 'password']
    print('teardown')


def pytest_generate_tests(metafunc: "Metafunc") -> None:
    if 'param' in metafunc.fixturenames:
        metafunc.parametrize('param',
                             metafunc.module.mydatas,
                             ids=metafunc.module.myids,
                             scope='function'
                             )


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    print(len(items))
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
