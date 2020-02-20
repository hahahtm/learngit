#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""author:hahahtm
   date:

"""
def square(x):
    '''
	计算平方并返回结果
	>>> square(2)
	4
	>>> square(3)
	9
	'''
    return x * x


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)