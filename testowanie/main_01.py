def test1_sum():
    try:
        assert sum([1, 2, 3]) == 6, "wyniki poprawny to 6"
    except AssertionError:
        print("nie udało się zakończyć testu 1")


def test2_sum():
    try:
        assert sum([1, 1, 1]) == 6, "wyniki poprawny to 6"
    except AssertionError:
        print("nie udało się zakończyć testu 2")

def tests():
    test1_sum()
    test2_sum()
    print("Udało się zakończyć test")

tests()