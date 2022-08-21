#! /usr/bin/env python
# -*- coding: utf-8 -*-

from usecase.runner import runner



def main():
    print(runner)
    runner.run()
    print("passed")


if __name__ == '__main__':
    main()