# -*- coding: utf-8 -*-
# 测试文件
import sys
from os.path import dirname, join
import pytest

#返回文件路径
# sys.path.append(dirname(dirname(__file__)))


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
        # cal = Calculator()
        assert result == self.cal.add(a, b)

    @pytest.mark.add
    def test_add1(self):
        # cal = Calculator()
        assert 3 == self.cal.add(4, 5)

    @pytest.mark.div
    def test_div(self):
        # cal = Calculator()
        assert 2 == self.cal.div(6, 3)
