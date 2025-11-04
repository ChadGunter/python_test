def reverse_string(word):
    return ''.join(reversed(word))

def test_reverse_string():
    input_str = "TripleTen"

    reverse_str = reverse_string(input_str)
    assert reverse_str == "neTelpirT"

    print("Test Passed! " + input_str + "'s reverse is " + reverse_str)