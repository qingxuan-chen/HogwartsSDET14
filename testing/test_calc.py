# -*- coding: utf-8 -*-
# 测试文件
import sys
from os.path import dirname, join
import pytest

# sys.path.append(dirname(dirname(__file__)))
import yaml

sys.path.append('E:/XUAN/HogwartsSDET14')

from pythoncode.calc import Calculator


def setup_module():
    print("模块级别setup")
    print('这个模块的路径是：' + dirname(__file__))


def teardown_module():
    print("模块级别teardown")


def setup_function():
    print("函数级别setup")


def teardown_function():
    print("函数级别teardown")


def test_case1():
    print("testcase1")


def get_steps():
    with open('steps/add.yml') as f:
        steps = yaml.safe_load(f)
    return steps


cal = Calculator()


def steps(a, b, result):
    steps1 = get_steps()
    for step in steps1:
        if 'add' == step:
            assert result == cal.add(a, b)
        elif 'add1' == step:
            assert result == cal.add1(a, b)
        elif 'add2' == step:
            assert result == cal.add2(a, b)


class TestCalc:
    def setup_class(self):
        self.cal = Calculator()
        print("类级别setup")

    def teardown_class(self):
        print("类级别teardown")

    def setup(self):
        # self.cal = Calculator()
        print("setup")

    def teardown(self):
        print("teardown")

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,result', [(1, 1, 2), (2, 1, 3)])
    def test_add(self, a, b, result):
        steps(a, b, result)
        # cal = Calculator()
        # assert result == self.cal.add(a, b)
        # assert result == self.cal.add1(a, b)
        # assert result == self.cal.add2(a, b)

    @pytest.mark.add
    def test_add1(self):
        # cal = Calculator()
        assert 10 == self.cal.add(4, 5)

    @pytest.mark.div
    def test_div(self):
        # cal = Calculator()
        assert 2 == self.cal.div(6, 3)
