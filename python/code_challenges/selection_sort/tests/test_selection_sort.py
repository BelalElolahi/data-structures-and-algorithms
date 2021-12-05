from selection_sort import __version__
from selection_sort.sort import insertion_sort



def test_version():
    assert __version__ == '0.1.0'



def test_sort_1():
    arr=[2, 1, 3, 60, 111,4523 , 9, 10, 30]
    actual = insertion_sort(arr)
    excepted = [1, 2, 3, 9, 10, 30, 60, 111, 4523]
    assert actual == excepted


def test_sort_2():
    arr=[20,18,12,8,5,-2]
    actual = insertion_sort(arr)
    excepted = [-2,5, 8, 12, 18, 20]
    assert actual == excepted




def test_sort_3():
    arr=[5,12,7,5,5,7]
    actual = insertion_sort(arr)
    excepted = [5, 5, 5, 7, 7, 12]
    assert actual == excepted



def test_sort_4():
    arr=[2,3,5,7,13,11]
    actual = insertion_sort(arr)
    excepted = [2,3,5,7,11,13]
    assert actual == excepted


