import yaml

with open('datas/a.yml', encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    myids = datas.keys()
    mydatas = datas.values()


def test_param(param):
    print(f'param = {param}')
    print("动态生成测试用例")
