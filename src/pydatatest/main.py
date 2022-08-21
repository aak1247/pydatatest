
from pydatatest.api import runner

from pydatatest.data.csv import get_data
from pydatatest.api import inject, inject_def, test, PyDataTestCase, run_with

myrunner = runner()

data = get_data('examples/data/csv/login.csv')


@test
@inject_def(['passport', 'password'], session=True)
@run_with(myrunner)
class TestUserLogin(PyDataTestCase):
    def setUp(self):
        print("login test start\n")

    @inject(data[0])
    def test_01(self):
        self.assertEqual(self.passport, 'hitest')

    @inject(data[0])
    def test_02(self):
        self.assertEqual(self.password, '111111')

    def tearDown(self):
        print("login test end\n")


def main():
    print(myrunner)
    myrunner.run()
    print("passed")


if __name__ == '__main__':
    main()