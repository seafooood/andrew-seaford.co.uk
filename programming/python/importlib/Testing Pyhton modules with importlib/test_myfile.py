# test_myfile.py
def test_function_one(mymodule):
    assert mymodule["functionOne"]() == 1

def test_function_two(mymodule):
    assert mymodule["functionTwo"]() == 2

def test_function_three(mymodule):
    assert mymodule["functionThree"](3, 4) == 7

def test_main(mymodule):
    assert mymodule["main"]() == 2
