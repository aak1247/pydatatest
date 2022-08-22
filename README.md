# PyDataTest
Data driven python test framework

# Document
## Introduction

Aim to provide a simple way to write testcase, especially when test same logic with different data input and output. So PyDataTest wrap unittest with a set of utilities to test with data.

## Install

```shell
pip install pydatatest # with pip
poetry add pydatatest # or with poetry
pipenv add pydatatest # with pipenv
```

## Usage
1. Get a runner instance
   ```python
    runner = pydatatest.runner()
   ```
2. Write a test case and inject data including input and output
    ```python
    data = [["abc","123"], ['aaa',"000000"]]

    @inject_def(['passport', 'password'], session=True)
    @test_with(runner) # Register this testcase, also can use runner name, eg: @test_with("runner1")
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
3. Run with PyDataTest
    ```python
    runner.run()
    ```



## API

`runner` 
> A framework instance that will run all testcases
> 
> Example:
> ```python
> r = pydatatest.runner("my runner")
> r.add_test(testcase) # add a test case manually
> r.run() # start test
> ```

`PyDataTestCase`
> Data test Instance
> 
> Attributes:
>   - **session**: request session, can be used in many test method to share some state
>   - **injected variables**: You can access it in your test method as self.variable_name(the name is as defined in your @inject_def)
>
> Methods:
>   - **before_all**: run before all cases
>   - **after_all**: run after all cases
>   - **before_each**: run before all run of every test method
>   - **after_each**: run before all run of every test method
>   - **before_each_data**: run before every run of every test method
>   - **after_each_data**: run after every run of every test method
>   - **test****: test case method, each method will be run several times accoding to the injected data
> 
>   You can also use the unittest api here, such as self.assertEqual, for more information, see [Assert methods](https://docs.python.org/3/library/unittest.html#assert-methods) and [unittest](https://docs.python.org/3/contents.html)
>
> Example:
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
>   def test_02(self):
>       print(self.passport)
>       print(self.password)
>       self.assertEqual(self.password, 'password')
> 
>   @inject(["username", "password1"])
>   def test_03(self):
>       self.assertEqual(self.password, 'password')
> ```

### @test_with
> Register a testcase
> 
> Params:
> - ``runner``: string or runner instance, you can use runner name to avoid loop dependency

### @inject_def and @inject
> Example：
> 
> ```python
> @inject_def(['passport', 'password'], session=True)
> class TestCaseClass(PyDataTestCase):
> @inject(["passport1", "password1"])
> def test_01(self):
>   print(self.passport) # defined variable can be access here
#### @inject_def
> Define inject data varibales
> Params:
> - ``variables``: injected data will be parsed according to the sequence of variables
> - ``session``: if True means that this case will use request session

#### @inject
> Inject data to a test method
> 
> Params:
>   - ``data``: list like data, will be parsed according to its sequence (same as ``@inject_def``)
>   - ``multi``: if true, the data will be seen as list of many group of variable, and this test method will be run the same times as the length of the data. Each group of variable will be run once.
# TODO
- [ ] @depends_on: to run multicase pipeline automatically
- [ ] @inject_yaml: to inject yaml data
- [ ] @inject_csv: to inject csv data
- [ ] @once: indicates that the test case should be run once
- [ ] @expected: indicates that the test case should return expected output
- [ ] @throws: indicates that the test case should throw specific exception
- [ ] More corner case