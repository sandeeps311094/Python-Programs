#---  A simple demonstration of the pytest test automation module of Python


import os
import pytest
import imp
from nltk import word_tokenize

def add (a, b):
    return (a + b)

def product (x, y):
    return (x * y)

def write_string_to_list (str1):
    ls = word_tokenize (str1)
    return (ls)

def get_i():
	fob = open("i_holder.txt", "r+")
	x = fob.read()

	x = int(x)
	y = str(x + 1)
	i = x

	fob = open("i_holder.txt", "w+")
	fob.write(y)
	fob.close()

	return (i)

#--

def test_get_i():
    x = '6'
    x = int(x)
    y = str(x + 1)
    i = x
    assert get_i() == 28

def test_add():
    assert add (10, 4) == 14
    assert add (3, 6)  == 9
    assert add (100, 5) == 105

def test_product():
    assert product (2, 5) == 10
    assert product (100, 9) == 900
    assert product (12, 12) == 144

def test_write_string_to_list():
    assert write_string_to_list ('The brown bear is sleeping') == ['The', 'brown', 'bear', 'is', 'sleeping']



if __name__ == '__main__':
    #test_add()
    #test_product()
    #test_write_string_to_list()

    test_get_i()
