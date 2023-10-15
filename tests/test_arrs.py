from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, None) == 2
    assert arrs.get([], 7, None) == None


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 0, -1) == [1, 2]
    assert arrs.my_slice([1, 2, 3], 0, 0) == []
    assert arrs.my_slice([1, 2, 3, 4], -1) == [4]
    assert arrs.my_slice([1, 2, 3, 4], 5) == []
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3, 4, 5, 6, 7, 8], 3, -1) == [4, 5, 6, 7]
    assert arrs.my_slice([1, 2, 3, 4], end=0) == []
    assert arrs.my_slice([1, 2, 3, 4, 5, 6, 7, 8], -1, 9) == [8]
    assert arrs.my_slice([1, 2, 3]) == [1, 2, 3]
