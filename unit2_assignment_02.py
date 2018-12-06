__author__ = 'Kalyan'

notes = '''
Write your own implementation of converting a number to a given base. It is important to have a good logical
and code understanding of this.

Till now, we were glossing over error checking, for this function do proper error checking and raise exceptions
as appropriate.

Reading material:
    http://courses.cs.vt.edu/~cs1104/number_conversion/convexp.html
'''

def convert(number, base):
    """
    Convert the given number into a string in the given base. valid base is 2 <= base <= 36
    raise except, YY) does (play in the console to find what errors it raises).
    Handle negative numbers just like bin and oct do.
    """
    if(2<=base<=36):

        list = []
        num = number
        if (number < 0):
            number = -number
        while number != 0:
            t = number % base
            number = int(number / base)
            if (0 <= t <= 9):
                list.append(str(t))
            elif (t >= 10):
                list.append(chr(55 + t))
        if (num < 0):
            list.append("-")
        list.reverse()
        p = "".join(list)
        return p
    elif(base<2 or base>36):
        raise ValueError
    elif("str"==type(base).__name__ or "str"==type(number).__name__ or number==None or base==None):
        raise TypeError

def test_convert():
    assert "100" == convert(4,2)
    assert "FF" == convert(255,16)
    assert "377" == convert(255, 8)
    assert "JJ" == convert(399, 20)
    assert "-JJ" == convert(-399, 20)

    try:
        convert(10,1)
        assert False, "Invalid base <2 did not raise error"
    except ValueError as ve:
        print(ve)

    try:
        convert(10, 40)
        assert False, "Invalid base >36 did not raise error"
    except ValueError as ve:
        print(ve)

    try:
        convert("100", 10)
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print(te)

    try:
        convert(None, 10)
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print(te)


    try:
        convert(100, "10")
        assert False, "Invalid base did not raise error"
    except TypeError as te:
        print(te)
