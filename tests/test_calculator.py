import sys
sys.path.insert(0, "src")

from calculator import add

def test_add():
    assert add(2, 3) == 5
