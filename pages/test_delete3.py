import pytest


@pytest.mark.parametrize("uname,passwrd",[("abc","qwe"),("rty","uio"),("zxc","vbn")])
def test_MessageTest(uname,passwrd):
    print(uname+"-"+passwrd)

@pytest.mark.smoke
def test_111():
    aa=51
    ab=52
    assert aa==ab,"3333.."