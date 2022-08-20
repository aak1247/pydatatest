# PyDataTest
Data driven python test framework

# Document
## Introduction

Aim to provide a simple way to write testcase, especially when test same logic with different data input and output. So PyDataTest wrap unittest with a set of utilities to test with data.

## Usage
1. Get a runner instance
   ```python
    runner = pydatatest.runner()
   ```
2. Write a test case and inject data including input and output
    ```python
    data = [["abc","123"], ['aaa',"000000"]]

    @test
    @inject_def(['passport', 'password'], session=True)
    @run_with(runner) # Register this testcase
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


## API

`runner` 
> A framework instance that will run all testcases
> Example:
> r = pydatatest.runner()
> r.run()


# TODO
- [ ] @depends_on: to run multicase pipeline automatically
- [ ] @inject_yaml: to inject yaml data
- [ ] @inject_csv: to inject csv data
- [ ] @once: indicates that the test case should be run once
- [ ] @after: indicates that the test case should run after another
- [ ] @expected: indicates that the test case should return expected output
- [ ] @throws: indicates that the test case should throw specific exception