# -*- coding: utf-8 -*-
# 测试文件
import sys

import pytest

sys.path.append('D:\\CHEN\\HogwartsSDET14')
from pythoncode.calc import Calculator


def setup_module():
    print("模块级别setup")


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
        print("setup")

    def teardown(self):
        print("teardown")

    @pytest.mark.add
    def test_add(self):
        # cal = Calculator()
        assert 2 == self.cal.add(1, 1)

    @pytest.mark.add
    def test_add1(self):
        # cal = Calculator()
        assert 3 == self.cal.add(2, 1)

    @pytest.mark.div
    def test_div(self):
        # cal = Calculator()
        assert 2 == self.cal.div(2, 1)
