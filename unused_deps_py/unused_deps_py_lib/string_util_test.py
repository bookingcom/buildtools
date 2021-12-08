import pytest
from string_util import remove_prefix

def test_remove_prefix():
    assert remove_prefix("//hello", "//") == "hello"
    assert remove_prefix("bye", "//") == "bye"

if __name__ == '__main__':
    raise SystemExit(pytest.main([__file__]))
