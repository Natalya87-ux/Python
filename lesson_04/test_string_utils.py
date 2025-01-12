import pytest

from stringutils import StringUtils

string_util = StringUtils()
# Test Case 1:


@pytest.mark.parametrize('string, result', [
    # positive test cases:
    ("peter", "Peter"),
    ("annMary", "Annmary"),
    ("mary Anne", "Mary anne"),
    ("ty'jan", "Ty'jan"),
    ("king1", "King1"),
    ("example-1", "Example-1"),
    # negative test cases:
    ("", ""),
    ("Steve", "Steve"),
    ("GPS", "Gps"),
    ("123abc", "123abc"),
    ("  leading space", "  leading space"),
    ("trailing space  ", "Trailing space  "),
    ("éxample", "Éxample")  # other alphabets
])
def test_capitalize(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.capitalize(string)
    print(f"Actual result: {res}")
    assert res == result

# Test Case 2:


@pytest.mark.parametrize('string, result', [
    # positive test cases:
    ("  dog", "dog"),
    (" ABC", "ABC"),
    ("  123  ", "123  "),
    (" Mary-Anne", "Mary-Anne"),
    ("   Peter1", "Peter1"),
    # negative test cases:
    ("", ""),
    ("ca t", "ca t"),
    ("monkey", "monkey"),
    ("123  ", "123  ")
])
def test_trim(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.trim(string)
    print(f"Actual result: {res}")
    assert res == result

# Test Case 3:


@pytest.mark.parametrize('string, divider, result', [
    # positive test cases:
    ("dog,cat,bird", ",", ["dog", "cat", "bird"]),
    ("flower,tree,forest", ",", ["flower", "tree", "forest"]),
    ("pen;pencil;marker", ";", ["pen", "pencil", "marker"]),
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),
    ("@^%^&^!^*", "^", ["@", "%", "&", "!", "*"]),
    ("1/n2/n3", "/n", ["1", "2", "3"]),
    # negative test cases:
    ("", None, []),
    ("1,2,3,4 5", None, ["1", "2", "3", "4 5"]),
])
def test_to_list(string, divider, result):
    print(f"Input string: {string}")
    print(f"Expected result: {result}")

    if divider is None:
        res = string_util.to_list(string)
    else:
        res = string_util.to_list(string, divider)

    print(f"Actual result: {res}")

    assert res == result

# Test Case 4:


@pytest.mark.parametrize('string, symbol, result', [
    # positive test cases:
    ("flower", "f", True),
    (" test", "t", True),
    ("space  ", "e", True),
    ("Mary-Anne", "-", True),
    ("123", "1", True),
    ("GPS", "P", True),
    ("", "", True),
    # negative test cases:
    ("City", "c", False),
    ("parameter", "P", False),
    ("hello", "x", False),
    ("hello", "!", False),
    ("", "x", False),
    ("hello", "xyz", False)
])
def test_contains(string, symbol, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Inputed symbol: {symbol}")
    print(f"Expected result: {result}")
    res = string_util.contains(string, symbol)
    print(f"Actual result: {res}")
    assert res == result

# Test Case 5:


@pytest.mark.parametrize('string, symbol, result', [
    # positive test cases:
    ("test", "t", "es"),
    ("Street", "r", "Steet"),
    ("Mountain", "M", "ountain"),
    ("123", "1", "23"),
    ("Mary-Anne", "-", "MaryAnne"),
    ("Sky Pro", " ", "SkyPro"),
    ("plate", "pla", "te"),
    # negative test cases:
    ("spoon", "k", "spoon"),
    ("", "", ""),
    ("", "g", ""),
    ("milk", "", "milk"),
    ("park ", " ", "park"),
    ("carpet  ", "r", "capet  ")
])
def test_delete_symbol(string, symbol, result):
    string_util = StringUtils()
    res = string_util.delete_symbol(string, symbol)
    assert res == result

# Test Case 6:


@pytest.mark.parametrize('string, symbol, result', [
    # positive test cases:
    ("table", "t", True),
    ("", "", True),
    ("Headphones", "H", True),
    (" car", "", True),
    ("Film  ", "F", True),
    ("Anne-Mary", "A", True),
    ("Mary Anne", "M", True),
    ("123", "1", True),
    ("list", "", True),
    # negative test cases:
    ("Headphones", "h", False),
    ("tea", "T", False),
    ("", "v", False),
    ("Test", "t", False),
    ("eleven", "n", False),
    ("twenty", "w", False)
])
def test_starts_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.starts_with(string, symbol)
    assert res == result

# Test Case 7:


@pytest.mark.parametrize('string, symbol, result', [
    # positive test cases:
    ("winter", "r", True),
    ("GREAT", "T", True),
    ("", "", True),
    ("cat ", "", True),
    ("123", "3", True),
    ("Mary-Anne", "e", True),
    ("Anne Mary", "y", True),
    ("Peter1", "1", True),
    ("test", "", True),
    # negative test cases:
    ("morning", "P", False),
    ("evening", "e", False),
    ("door", "R", False),
    ("", "n", False)
])
def test_end_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.end_with(string, symbol)
    assert res == result

# Test Case 8:


@pytest.mark.parametrize('string, result', [
    # positive test cases:
    ("", True),
    (" ", True),
    ("  ", True),
    # negative test cases:
    ("tree", False),
    (" flower", False),
    ("123", False),
    ("cat ", False)
])
def test_is_empty(string, result):
    string_util = StringUtils()
    res = string_util.is_empty(string)
    assert res == result

# Test Case 9:


@pytest.mark.parametrize('lst, joiner, result', [
    # positive test cases:
    (["a", "b", "c"], ",", "a,b,c"),
    ([1, 2, 3, 4, 5], None, "1, 2, 3, 4, 5"),
    (["a", "b", "c"], "", "abc"),
    (["Mary", "Anne"], "-", "Mary-Anne"),
    # negative test cases:
    ([], None, ""),
    ([], "*", "")
])
def test_list_to_string(lst, joiner, result):
    string_util = StringUtils()
    print(f"Input list: {lst}")
    print(f"Expected result: {result}")
    if joiner is None:
        res = string_util.list_to_string(lst)
    else:
        res = string_util.list_to_string(lst, joiner)
    print(f"Actual result: {res}")
    assert res == result
