from incertezze import Number

a = Number(10, 1)
b = Number(5, 1)
c = Number(10, relative_error=0.1)
d = Number(5, relative_error=0.2)

def test_absolute_sum():
    assert a + b == Number(15, 2)
    
def test_absolute_sub():
    assert a - b == Number(5, 2)
    
def test_absolute_mul():
    assert a * b == Number(50, relative_error=0.3)
    
def test_absolute_div():
    assert a / b == Number(2, relative_error=0.3)
    
def test_relative_sum():
    assert a + b == Number(15, 2)
    
def test_relative_sub():
    assert a - b == Number(5, 2)
    
def test_relative_mul():
    assert a * b == Number(50, 2)
    
def test_relative_div():
    assert a / b == Number(2, 2)