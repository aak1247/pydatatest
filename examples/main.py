#! /usr/bin/env python
# -*- coding: utf-8 -*-

from usecase.runner import myrunner



def main():
    print(myrunner)
    myrunner.run()
    print("passed")


if __name__ == '__main__':
    main()