from main import *

def foo(x):
    if x<=1:
      return x
    else: 
      return foo(x-1)+foo(x-2)
    pass

def test_foo():
    assert foo(10) == 55

def test_foo2():
    assert foo(0) == 0
    assert foo(1) == 1

test_foo()
test_foo2()
