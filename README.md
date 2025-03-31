# PyDataTest

数据驱动的Python测试框架

![PyPI](https://img.shields.io/pypi/v/pydatatest)
![License](https://img.shields.io/github/license/aak1247/PyDataTest)

| [English](./README.en-US.md) | 简体中文 |

# 文档
## 简介

旨在提供一种编写测试用例的简单方法，尤其是在使用不同的数据输入和输出测试相同的逻辑时。因此，PyDataTest 提供了一套工具用来基于数据进行测试。

## 安装

```shell
pip install pydatatest # with pip
poetry add pydatatest # or with poetry
pipenv add pydatatest # with pipenv
```

## 使用
1. 创建一个runner实例
   ```python
    runner = pydatatest.runner()
   ```
2. 编写一个测试用例并注入数据，包括输入和输出
    ```python
    data = [["abc","123"], ['aaa',"000000"]]

    @inject_def(['passport', 'password'], session=True)
    @test_with(runner) # 注册用例，也可以通过runner名称进行注册, 如: @test_with("runner1")
    class TestUserLogin(PyDataTestCase):
        def setUp(self):
        print("login test start\n")

        @inject(["abc", "123456"])
        def test_01(self):
            self.assertEqual(self.passport, 'hitest')

        @inject(data, True)
        def test_02(self):
            self.assertEqual(self.password, '111111')

        def tearDown(self):
            print("login test end\n")
    ```
3. 通过PyDataTest运行起来
    ```python
    runner.run()
    ```



## API

`runner` 
> 框架实例，用来运行所有的测试用例
> 
> Example:
> ```python
> r = pydatatest.runner("my runner")
> r.add_test(testcase) # 手动添加一个测试用例
> r.run() # 运行所有测试用例
> ```

`PyDataTestCase`
> 测试用例组，用来组织测试用例
> 
> 属性:
>   - **session**: 获取session, 可以用来在不同的用例方法之间传递数据和共享状态（尤其是HTTP的登录状态等）
>   - **injected variables**: 可以在用例方法中通过 self.variable_name(通过@inject_def声明的变量名)来访问注入的数据
>
> 方法:
>   - **before_all**: 在所有用例方法之前运行(只运行一次)
>   - **after_all**: 在所有用例方法之后运行（只运行一次）
>   - **before_each**: 在每个用例方法之前运行（对每个方法的多组数据只执行一次）
>   - **after_each**: 在每个用例方法之后运行（对每个方法的多组数据只执行一次）
>   - **before_each_data**: 在每组数据被执行前运行
>   - **after_each_data**: 在每组数据被执行后运行
>   - **test****: 测试用例方法, 以test开头的方法都会被认为是测试用例方法，可以通过@inject注入数据，将会根据注入数据的数量执行多次
> 
>  在用例方法中可以使用``unittest``的``API``, 比如self.assertEqual, 详见 [Assert methods](https://docs.python.org/3/library/unittest.html#assert-methods) 和 [unittest](https://docs.python.org/3/contents.html)
>
> 样例:
> ```python
> @inject_def(['passport', 'password'], session=True)
> @test_with(myrunner)
> class TestUserLogin(PyDataTestCase):
>   @classmethod
>   def before_all(cls):
>       print("before all test")
> 
>   @classmethod
>   def after_all(cls):
>       print("after all test")
>       
>   def before_each(self):
>       print("before_each test")
>   
>   def after_each(self):
>       print("after_each test")
> 
>   def before_each_data(self):
>       print("before_each_data test")
>   
>   def after_each_data(self):
>       print("after_each_data test")
> 
>   @inject(data[0])
>   def test_01(self):
>       self.assertEqual(self.passport, 'username')
> 
> 
>   @inject(data, multi=True)
>   def test_02(self): # 这条用例会被执行多次
>       print(self.passport)
>       print(self.password)
>       self.assertEqual(self.password, 'password')
> 
>   @inject(["username", "password1"])
>   def test_03(self):
>       self.assertEqual(self.password, 'password')
> ```

### @test_with
> 注册测试用例到runner的注解
> 
> Params:
> - ``runner``: 字符串或runner实例, 如果是字符串则会从全局runner中查找，可以通过传入字符串来避免循环引用

### @inject_def and @inject
> 数据定义和注入注解
> Example：
> 
> ```python
> @inject_def(['passport', 'password'], session=True)
> class TestCaseClass(PyDataTestCase):
> @inject(["passport1", "password1"])
> def test_01(self):
>   print(self.passport) # @inject_def中声明的变量
#### @inject_def
> 定义要注入的数据变量
> Params:
> - ``variables``: 注入的数据将会根据变量的声明顺序进行解析
> - ``session``: bool, 如果为True表示该用例将会启用request session, 详见 [requests](https://requests.readthedocs.io/en/master/user/advanced/#session-objects)

#### @inject
> 注入数据到测试用例方法
> 
> Params:
>   - ``data``: list like的数据，将会按照顺序进行解析 (same as ``@inject_def``)
>   - ``multi``: 如果为True, 则会将数据解析为多组数据，每组数据将会被执行一次

# 待改进的地方
- [ ] @depends_on: to run multicase pipeline automatically
- [ ] @inject_yaml: to inject yaml data
- [ ] @inject_csv: to inject csv data
- [ ] @once: indicates that the test case should be run once
- [ ] @expected: indicates that the test case should return expected output
- [ ] @throws: indicates that the test case should throw specific exception
- [ ] More corner case 

# 开发


## 安装依赖
```shell
pyenv local 3.9.13
poetry install
```

## 运行测试
```shell
cd examples
poetry run python main.py
```

## 发布
```shell
poetry publish --build
```