import pytest
from currency import usd

@pytest.mark.parametrize("input,output", [
    (1, "$1.00"),
    (11.5, "$11.50"),
    (1.75, "$1.75"),
    (1200.751, "$1,200.75"),
    (-1245.758, "-$1,245.76"),
    (-1.754, "-$1.75")
])
def test_usd(input, output):
    assert usd(input) == output